# core/views.py

from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, BusinessProfileForm
from .models import CustomUser, BusinessProfile
from django.contrib.auth.hashers import make_password, check_password
import openai
from django.conf import settings
from django.shortcuts import render
from .models import BusinessProfile, CustomUser
import cohere
from django.shortcuts import render, redirect
from .models import CustomUser, BusinessProfile
import os
from dotenv import load_dotenv
load_dotenv()
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))


def home_view(request):
    return render(request, 'core/home.html')


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, BusinessProfileForm

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, BusinessProfileForm
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        print("method was post")
        user_form = RegisterForm(request.POST)
        profile_form = BusinessProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            print("entered saving space")

            # Hash password before saving
            user.password = make_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # ✅ Redirect to login page after successful registration
            return redirect('login')
        else:
            print("User form errors:", user_form.errors)
            print("Profile form errors:", profile_form.errors)
    else:
        print("not post")
        user_form = RegisterForm()
        profile_form = BusinessProfileForm()

    return render(request, 'core/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(username=username)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    print("A")
                    return redirect('dashboard')
                
                else:
                    form.add_error(None, 'Invalid password')
            except CustomUser.DoesNotExist:
                form.add_error(None, 'User does not exist')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    return redirect('login')


def dashboard_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = CustomUser.objects.get(id=user_id)
    try:
        profile = BusinessProfile.objects.get(user=user)
    except BusinessProfile.DoesNotExist:
        profile = None
    return render(request, 'core/dashboard.html', {'user': user, 'profile': profile})


def ai_suggestions_view(request):
    return render(request, 'core/ai_suggestions.html')

def feedback_view(request):
    return render(request, "core/feedback.html")


openai.api_key = "your-openai-key"  # Will be moved to settings later
import openai
from django.shortcuts import render, redirect
from .models import CustomUser, BusinessProfile

# ✅ This uses the new OpenAI client style
client = openai.OpenAI(api_key="your-openai-api-key")  # Replace with your real key or use env variable
import os
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# core/views.py

import openai
from django.conf import settings
from django.shortcuts import render, redirect
from .models import CustomUser, BusinessProfile

# openai.api_key = settings.OPENAI_API_KEY  
# # ✅ Set API key

co = cohere.Client(os.getenv("COHERE_API_KEY"))

import cohere
import os
from django.shortcuts import render, redirect
from .models import CustomUser, BusinessProfile

cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

def ai_suggestions_view(request):
    if not request.session.get('user_id'):
        return redirect('login')

    user = CustomUser.objects.get(id=request.session['user_id'])
    profile = BusinessProfile.objects.get(user=user)

    marketing_text = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        language = request.POST.get("language", "english")
        length = request.POST.get("length", "small")

        # Token limit based on length
        token_map = {
            "small": 60,
            "medium": 150,
            "long": 300
        }
        max_tokens = token_map.get(length, 100)

        prompt = f"""
        Generate a marketing message in {language} for a beauty parlour named '{profile.business_name}'.
        This parlour offers: {profile.description}.
        Focus on: {user_input}.
        Make it friendly, catchy, and suitable for WhatsApp, Instagram, or Facebook.
        Include emojis if appropriate. Limit to a {length} message.
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
            marketing_text = f"❌ Error from Cohere: {str(e)}"

    return render(request, 'core/ai_suggestions.html', {
        'marketing_text': marketing_text,
        'profile': profile,
        'user': user
    })




# def ai_suggestions_view(request):
#     if not request.session.get('user_id'):
#         return redirect('login')

#     user = CustomUser.objects.get(id=request.session['user_id'])
#     profile = BusinessProfile.objects.get(user=user)

#     marketing_text = ""

#     if request.method == "POST":
#         user_input = request.POST.get("user_input", "")  # Get additional focus input

#         prompt = f"""
#         Generate a short, engaging marketing message for a beauty parlour named '{profile.business_name}'.
#         This parlour offers: {profile.description}.
#         Focus on: {user_input}.
#         Make it friendly, catchy, and suitable for WhatsApp, Instagram, or Facebook.
#         Include emojis if appropriate. Limit it to 2 short paragraphs.
#         """

#         try:
#             response = openai.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You're a helpful marketing assistant."},
#                     {"role": "user", "content": prompt}
#                 ],
#                 max_tokens=300,
#                 temperature=0.7,
#             )
#             marketing_text = response.choices[0].message.content.strip()

#         except Exception as e:
#             marketing_text = f"❌ Error from OpenAI: {str(e)}"

#     return render(request, 'core/ai_suggestions.html', {
#         'marketing_text': marketing_text,
#         'profile': profile,
#         'user': user
#     })
