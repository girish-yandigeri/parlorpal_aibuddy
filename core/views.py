# core/views.py

from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, BusinessProfileForm
from .models import CustomUser, BusinessProfile
# from django.contrib.auth.hashers import make_password, check_password
import openai
from django.conf import settings
from django.shortcuts import render
from .models import BusinessProfile, CustomUser
import cohere
from django.shortcuts import render, redirect
from .models import CustomUser, BusinessProfile
import os
from dotenv import load_dotenv
import os
import cohere
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
import cohere
import os
from django.shortcuts import render, redirect
from .models import CustomUser, BusinessProfile
import cloudinary.uploader
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, BusinessProfileForm
from .models import CustomUser, BusinessProfile
from django.contrib import messages
from django.http import HttpResponse
import os, uuid
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from dotenv import load_dotenv
import cohere

load_dotenv()
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

def home_view(request):
    return render(request, 'core/home.html')

def register_view(request):
    if request.method == 'POST':
        print("POST received")
        user_form = RegisterForm(request.POST)
        profile_form = BusinessProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            print("✅ Forms are valid")
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
        else:
            print("❌ User form errors:", user_form.errors)
            print("❌ Profile form errors:", profile_form.errors)
    else:
        user_form = RegisterForm()
        profile_form = BusinessProfileForm()
    
    return render(request, 'core/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    profile = BusinessProfile.objects.filter(user=request.user).first()
    return render(request, 'core/dashboard.html', {'user': request.user, 'profile': profile})

@login_required
def ai_suggestions_view(request):
    profile = BusinessProfile.objects.get(user=request.user)
    marketing_text = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        language = request.POST.get("language", "english")
        length = request.POST.get("length", "small")

        token_map = {"small": 120, "medium": 250, "long": 500}
        max_tokens = token_map.get(length, 100)
        
        
        prompt = f"""
Task: Output only a social media caption for a beauty parlour.
Language: {language}
Character Limit: {length}

Business Name: {profile.business_name}
Services: {profile.description}
Focus: {user_input}
Platform: Instagram, WhatsApp, or Facebook

Instructions:
- Output only the caption text. Do NOT include any explanation, intro, or extra commentary.
- Use at least 4 attractive and relevant emojis related to beauty, sparkle, or care (like 💅 💖 💇‍♀️ ✨ 💎).
- The output must be directly usable as a social media post caption.

Only print the final caption. Nothing else.
"""

        
        
        # prompt = f"""
        # Generate a marketing message in {language} for a beauty parlour named '{profile.business_name}'.
        # This parlour offers: {profile.description}.
        # Focus on: {user_input}.
        # Make it friendly, catchy, and suitable for WhatsApp, Instagram, or Facebook.
        # Include emojis if appropriate. Limit to a {length} message.
        # """

        try:
            print(prompt)
            response = cohere_client.generate(
                model="command",
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.7
            )
            marketing_text = response.generations[0].text.strip()
        except Exception as e:
            marketing_text = f"❌ Error from Cohere: {str(e)}"

    return render(request, 'core/ai_suggestions.html', {
        'marketing_text': marketing_text,
        'profile': profile,
        'user': request.user
    })

@login_required
def feedback_view(request):
    return render(request, "core/feedback.html")

@login_required


def poster_generator_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        profile = BusinessProfile.objects.get(user=request.user)
    except BusinessProfile.DoesNotExist:
        return redirect('dashboard')

    poster_url = None
    error_message = None

    if request.method == 'POST':
        user_input = request.POST.get("user_input", "")
        language = request.POST.get("language", "en")
        length = request.POST.get("length", "medium")
        theme_color = request.POST.get("theme_color", "lightpink")
        heading = request.POST.get("heading", "✨ Special Offer ✨")
        font_size_map = {"small": 10, "medium": 20, "large": 30}
        font_size_label = request.POST.get("font_size", "medium")
        font_size = font_size_map.get(font_size_label.lower(), 20)

        logo_file = request.FILES.get('logo')
        logo_url = profile.image.url if not logo_file and profile.image else None

        token_map = {"short": 80, "medium": 150, "long": 250}
        max_tokens = token_map.get(length.lower(), 150)
        language_instruction = "Translate this into Kannada." if language == "kn" else ""

        prompt = f"""
        Generate a {length} marketing message for a business named '{profile.business_name}'.
        This business offers: {profile.description}.
        Focus on: {user_input}.
        Make it friendly, catchy, suitable for Instagram, WhatsApp, and Facebook. Include emojis.
        {language_instruction}
        """

        try:
            response = cohere_client.generate(
                model="command",
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.7
            )
            marketing_text = response.generations[0].text.strip()
        except Exception as e:
            error_message = f"❌ Error from Cohere: {str(e)}"
            return render(request, 'core/generate_poster.html', {
                'user': request.user,
                'profile': profile,
                'poster_url': None,
                'error_message': error_message
            })

        # 🖼️ Generate the image
        img = Image.new("RGB", (800, 1000), color=theme_color)
        draw = ImageDraw.Draw(img)

        try:
            font_path = os.path.join("core", "static", "core", "Roboto-Bold.ttf")
            font = ImageFont.truetype(font_path, font_size)
        except:
            font = ImageFont.load_default()

        draw.text((40, 60), heading, fill="black", font=font)
        draw.text((40, 150), profile.business_name, fill="black", font=font)
        draw.text((40, 230), marketing_text, fill="black", font=font)

        # 👩‍🎨 Add logo (from upload or profile)
        try:
            if logo_file:
                logo_img = Image.open(logo_file)
            elif logo_url:
                from urllib.request import urlopen
                logo_img = Image.open(urlopen(logo_url))
            else:
                logo_img = None

            if logo_img:
                logo_img = logo_img.resize((150, 150))
                img.paste(logo_img, (600, 60))
        except Exception as e:
            print(f"Logo error: {e}")

        # ☁️ Upload to Cloudinary
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        try:
            upload_result = cloudinary.uploader.upload(
                buffer,
                folder="posters/",
                public_id=f"poster_{uuid.uuid4().hex}",
                overwrite=True,
                resource_type="image"
            )
            poster_url = upload_result.get('secure_url')
        except Exception as e:
            error_message = f"❌ Cloudinary Upload Failed: {str(e)}"

    return render(request, 'core/generate_poster.html', {
        'user': request.user,
        'profile': profile,
        'poster_url': poster_url,
        'error_message': error_message
    })

from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK")


















# load_dotenv()
# cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))


# def home_view(request):
#     return render(request, 'core/home.html')


# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from .forms import RegisterForm, BusinessProfileForm

# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from .forms import RegisterForm, BusinessProfileForm
# from .models import CustomUser

# def register_view(request):
#     if request.method == 'POST':
#         print("method was post")
#         user_form = RegisterForm(request.POST)
#         profile_form = BusinessProfileForm(request.POST, request.FILES)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)
#             print("entered saving space")

#             # Hash password before saving
#             user.password = make_password(user_form.cleaned_data['password'])
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()

#             #  Redirect to login page after successful registration
#             return redirect('login')
#         else:
#             print("User form errors:", user_form.errors)
#             print("Profile form errors:", profile_form.errors)
#     else:
#         print("not post")
#         user_form = RegisterForm()
#         profile_form = BusinessProfileForm()

#     return render(request, 'core/register.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             try:
#                 user = CustomUser.objects.get(username=username)
#                 if check_password(password, user.password):
#                     request.session['user_id'] = user.id
#                     print("A")
#                     return redirect('dashboard')
                
#                 else:
#                     form.add_error(None, 'Invalid password')
#             except CustomUser.DoesNotExist:
#                 form.add_error(None, 'User does not exist')
#     else:
#         form = LoginForm()
#     return render(request, 'core/login.html', {'form': form})


# def logout_view(request):
#     request.session.flush()
#     return redirect('login')


# def dashboard_view(request):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         return redirect('login')
#     user = CustomUser.objects.get(id=user_id)
#     try:
#         profile = BusinessProfile.objects.get(user=user)
#     except BusinessProfile.DoesNotExist:
#         profile = None
#     return render(request, 'core/dashboard.html', {'user': user, 'profile': profile})


# def ai_suggestions_view(request):
#     return render(request, 'core/ai_suggestions.html')

# def feedback_view(request):
#     return render(request, "core/feedback.html")


# openai.api_key = "your-openai-key"  # Will be moved to settings later
# import openai
# from django.shortcuts import render, redirect
# from .models import CustomUser, BusinessProfile

# #  This uses the new OpenAI client style
# client = openai.OpenAI(api_key="your-openai-api-key")  # Replace with your real key or use env variable
# import os
# client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# # core/views.py

# import openai
# from django.conf import settings
# from django.shortcuts import render, redirect
# from .models import CustomUser, BusinessProfile

# # openai.api_key = settings.OPENAI_API_KEY  
# # #  Set API key

# co = cohere.Client(os.getenv("COHERE_API_KEY"))

# import cohere
# import os
# from django.shortcuts import render, redirect
# from .models import CustomUser, BusinessProfile

# cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

# def ai_suggestions_view(request):
#     if not request.session.get('user_id'):
#         return redirect('login')

#     user = CustomUser.objects.get(id=request.session['user_id'])
#     profile = BusinessProfile.objects.get(user=user)

#     marketing_text = ""

#     if request.method == "POST":
#         user_input = request.POST.get("user_input", "")
#         language = request.POST.get("language", "english")
#         length = request.POST.get("length", "small")

#         # Token limit based on length
#         token_map = {
#             "small": 60,
#             "medium": 150,
#             "long": 300
#         }
#         max_tokens = token_map.get(length, 100)

#         prompt = f"""
#         Generate a marketing message in {language} for a beauty parlour named '{profile.business_name}'.
#         This parlour offers: {profile.description}.
#         Focus on: {user_input}.
#         Make it friendly, catchy, and suitable for WhatsApp, Instagram, or Facebook.
#         Include emojis if appropriate. Limit to a {length} message.
#         """

#         try:
#             response = cohere_client.generate(
#                 model="command",
#                 prompt=prompt,
#                 max_tokens=max_tokens,
#                 temperature=0.7
#             )
#             marketing_text = response.generations[0].text.strip()

#         except Exception as e:
#             marketing_text = f"❌ Error from Cohere: {str(e)}"

#     return render(request, 'core/ai_suggestions.html', {
#         'marketing_text': marketing_text,
#         'profile': profile,
#         'user': user
#     })




# # def ai_suggestions_view(request):
# #     if not request.session.get('user_id'):
# #         return redirect('login')

# #     user = CustomUser.objects.get(id=request.session['user_id'])
# #     profile = BusinessProfile.objects.get(user=user)

# #     marketing_text = ""

# #     if request.method == "POST":
# #         user_input = request.POST.get("user_input", "")  # Get additional focus input

# #         prompt = f"""
# #         Generate a short, engaging marketing message for a beauty parlour named '{profile.business_name}'.
# #         This parlour offers: {profile.description}.
# #         Focus on: {user_input}.
# #         Make it friendly, catchy, and suitable for WhatsApp, Instagram, or Facebook.
# #         Include emojis if appropriate. Limit it to 2 short paragraphs.
# #         """

# #         try:
# #             response = openai.chat.completions.create(
# #                 model="gpt-3.5-turbo",
# #                 messages=[
# #                     {"role": "system", "content": "You're a helpful marketing assistant."},
# #                     {"role": "user", "content": prompt}
# #                 ],
# #                 max_tokens=300,
# #                 temperature=0.7,
# #             )
# #             marketing_text = response.choices[0].message.content.strip()

# #         except Exception as e:
# #             marketing_text = f"❌ Error from OpenAI: {str(e)}"

# #     return render(request, 'core/ai_suggestions.html', {
# #         'marketing_text': marketing_text,
# #         'profile': profile,
# #         'user': user
# #     })




# load_dotenv()
# cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

# from PIL import Image, ImageDraw, ImageFont
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import CustomUser, BusinessProfile
# import os, uuid
# from io import BytesIO
# from dotenv import load_dotenv
# import cohere

# load_dotenv()
# cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

# def poster_generator_view(request):
#     if not request.session.get('user_id'):
#         return redirect('login')

#     user = CustomUser.objects.get(id=request.session['user_id'])
#     profile = BusinessProfile.objects.get(user=user)

#     poster_url = None
#     error_message = None

#     if request.method == 'POST':
#         user_input = request.POST.get("user_input", "")
#         language = request.POST.get("language", "en")
#         length = request.POST.get("length", "medium")
#         theme_color = request.POST.get("theme_color", "lightpink")
#         heading = request.POST.get("heading", "✨ Special Offer ✨")
#         # font_size = int(request.POST.get("font_size", 28))
#         # Map font size labels to pixel values
#         font_size_map = {
#             "small": 10,
#             "medium": 20,
#             "large": 30
#         }
#         font_size_label = request.POST.get("font_size", "medium")  # default to 'medium'
#         font_size = font_size_map.get(font_size_label.lower(), 20)  # fallback to 20px


#         logo = request.FILES.get('logo')
#         if not logo and profile.image:
#             logo = profile.image.path if os.path.exists(profile.image.path) else None

#         token_map = {"short": 80, "medium": 150, "long": 250}
#         max_tokens = token_map.get(length.lower(), 150)

#         language_instruction = "Translate this into Kannada." if language == "kn" else ""

#         prompt = f"""
#         Generate a {length} marketing message for a beauty parlour named '{profile.business_name}'.
#         This parlour offers: {profile.description}.
#         Focus on: {user_input}.
#         Make it friendly, catchy, suitable for Instagram, WhatsApp, and Facebook. Include emojis.
#         {language_instruction}
#         """

#         try:
#             response = cohere_client.generate(
#                 model="command",
#                 prompt=prompt,
#                 max_tokens=max_tokens,
#                 temperature=0.7
#             )
#             marketing_text = response.generations[0].text.strip()
#         except Exception as e:
#             error_message = f"❌ Error from Cohere: {str(e)}"
#             return render(request, 'core/generate_poster.html', {
#                 'user': user,
#                 'profile': profile,
#                 'poster_url': None,
#                 'error_message': error_message
#             })

#         # 🖼️ Poster
#         img = Image.new("RGB", (800, 1000), color=theme_color)
#         draw = ImageDraw.Draw(img)

#         try:
#             font_path = os.path.join("core", "static", "core", "Roboto-Bold.ttf")
#             font = ImageFont.truetype(font_path, font_size)
#         except:
#             font = ImageFont.load_default()

#         draw.text((40, 60), heading, fill="black", font=font)
#         draw.text((40, 150), profile.business_name, fill="black", font=font)
#         draw.text((40, 230), marketing_text, fill="black", font=font)

#         if logo:
#             try:
#                 logo_img = Image.open(logo)
#                 logo_img = logo_img.resize((150, 150))
#                 img.paste(logo_img, (600, 60))
#             except:
#                 pass  # skip if invalid logo

#         filename = f"poster_{uuid.uuid4().hex}.png"
#         poster_path = os.path.join('media', 'uploads', filename)
#         img.save(poster_path)
#         poster_url = f"/media/uploads/{filename}"

#     return render(request, 'core/generate_poster.html', {
#         'user': user,
#         'profile': profile,
#         'poster_url': poster_url,
#         'error_message': error_message
#     })
