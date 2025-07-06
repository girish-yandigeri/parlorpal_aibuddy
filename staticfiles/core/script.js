// // ParlorPal - Interactive JavaScript Features
// // Modern, responsive interactions for beauty salon AI marketing tool

// document.addEventListener('DOMContentLoaded', function() {
    
//     // =============================================================================
//     // FORM VALIDATION & ENHANCEMENT
//     // =============================================================================
    
//     // Enhanced form validation with real-time feedback
//     function initFormValidation() {
//         const forms = document.querySelectorAll('.needs-validation, .auth-form, .feedback-form');
        
//         forms.forEach(form => {
//             // Real-time validation
//             const inputs = form.querySelectorAll('input, textarea, select');
//             inputs.forEach(input => {
//                 input.addEventListener('blur', validateField);
//                 input.addEventListener('input', clearFieldError);
//             });
            
//             // Form submission with loading state
//             form.addEventListener('submit', handleFormSubmit);
//         });
//     }
    
//     // Validate individual field
//     function validateField(e) {
//         const field = e.target;
//         const value = field.value.trim();
        
//         // Clear previous validation
//         field.classList.remove('is-valid', 'is-invalid');
        
//         // Email validation
//         if (field.type === 'email') {
//             const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//             if (value && !emailRegex.test(value)) {
//                 showFieldError(field, 'Please enter a valid email address');
//                 return false;
//             }
//         }
        
//         // Password validation
//         if (field.type === 'password' && field.name === 'password') {
//             if (value && value.length < 8) {
//                 showFieldError(field, 'Password must be at least 8 characters long');
//                 return false;
//             }
//         }
        
//         // Password confirmation
//         if (field.name === 'confirmPassword') {
//             const password = document.querySelector('input[name="password"]');
//             if (password && value !== password.value) {
//                 showFieldError(field, 'Passwords do not match');
//                 return false;
//             }
//         }
        
//         // Required field validation
//         if (field.required && !value) {
//             showFieldError(field, 'This field is required');
//             return false;
//         }
        
//         // Mark as valid
//         field.classList.add('is-valid');
//         return true;
//     }
    
//     // Show field error
//     function showFieldError(field, message) {
//         field.classList.add('is-invalid');
//         const feedback = field.parentNode.querySelector('.invalid-feedback');
//         if (feedback) {
//             feedback.textContent = message;
//         }
//     }
    
//     // Clear field error on input
//     function clearFieldError(e) {
//         const field = e.target;
//         if (field.classList.contains('is-invalid')) {
//             field.classList.remove('is-invalid');
//         }
//     }
    
//     // =============================================================================
//     // LOADING ANIMATIONS & FORM SUBMISSION
//     // =============================================================================
    
//     // Handle form submission with loading state
//     function handleFormSubmit(e) {
//         const form = e.target;
//         const submitBtn = form.querySelector('button[type="submit"]');
//         const spinner = submitBtn.querySelector('.spinner-border');
        
//         // Show loading state
//         if (submitBtn && spinner) {
//             submitBtn.disabled = true;
//             spinner.classList.remove('d-none');
            
//             // For demo purposes, simulate loading
//             setTimeout(() => {
//                 submitBtn.disabled = false;
//                 spinner.classList.add('d-none');
//             }, 2000);
//         }
        
//         // Validate form before submission
//         if (!validateForm(form)) {
//             e.preventDefault();
//             return false;
//         }
//     }
    
//     // Validate entire form
//     function validateForm(form) {
//         const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
//         let isValid = true;
        
//         inputs.forEach(input => {
//             if (!validateField({ target: input })) {
//                 isValid = false;
//             }
//         });
        
//         return isValid;
//     }
    
//     // =============================================================================
//     // AI SUGGESTIONS PAGE FUNCTIONALITY
//     // =============================================================================
    
//     // AI Suggestions form handling
//     function initAISuggestions() {
//         const aiForm = document.getElementById('aiSuggestionForm');
//         const aiResults = document.getElementById('aiResults');
//         const templateCards = document.querySelectorAll('.template-card');
        
//         if (aiForm) {
//             aiForm.addEventListener('submit', handleAISubmission);
//         }
        
//         // Quick template selection
//         templateCards.forEach(card => {
//             card.addEventListener('click', function() {
//                 const template = this.getAttribute('data-template');
//                 const promptField = document.getElementById('prompt');
//                 if (promptField && template) {
//                     promptField.value = template;
//                     promptField.focus();
                    
//                     // Animate selection
//                     this.style.transform = 'scale(0.95)';
//                     setTimeout(() => {
//                         this.style.transform = 'scale(1)';
//                     }, 150);
//                 }
//             });
//         });
        
//         // Copy result functionality
//         const copyBtn = document.getElementById('copyResult');
//         if (copyBtn) {
//             copyBtn.addEventListener('click', copyAIResult);
//         }
//     }
    
//     // Handle AI form submission
//     function handleAISubmission(e) {
//         e.preventDefault();
        
//         const form = e.target;
//         const resultsCard = document.getElementById('aiResults');
//         const loadingAnimation = resultsCard.querySelector('.loading-animation');
//         const generatedContent = resultsCard.querySelector('.generated-content');
        
//         // Show results card
//         resultsCard.classList.remove('d-none');
//         loadingAnimation.classList.remove('d-none');
//         generatedContent.classList.add('d-none');
        
//         // Scroll to results
//         resultsCard.scrollIntoView({ behavior: 'smooth' });
        
//         // Simulate AI processing
//         setTimeout(() => {
//             loadingAnimation.classList.add('d-none');
//             generatedContent.classList.remove('d-none');
            
//             // Update content type badge
//             const contentType = form.querySelector('input[name="contentType"]:checked');
//             const badge = document.getElementById('contentTypeBadge');
//             if (contentType && badge) {
//                 const typeMap = {
//                     'social': 'Social Media Post',
//                     'email': 'Email Marketing',
//                     'promotion': 'Promotional Content',
//                     'general': 'General Copy'
//                 };
//                 badge.textContent = typeMap[contentType.value] || 'Generated Content';
//             }
//         }, 3000);
//     }
    
//     // Copy AI result to clipboard
//     function copyAIResult() {
//         const contentText = document.getElementById('generatedText');
//         if (contentText) {
//             const text = contentText.innerText;
//             navigator.clipboard.writeText(text).then(() => {
//                 showToast('Content copied to clipboard!', 'success');
//             });
//         }
//     }
    
//     // =============================================================================
//     // FEEDBACK PAGE FUNCTIONALITY
//     // =============================================================================
    
//     // Feedback form enhancements
//     function initFeedbackForm() {
//         const feedbackForm = document.getElementById('feedbackForm');
//         const messageField = document.getElementById('message');
//         const charCount = document.getElementById('charCount');
//         const starRating = document.querySelector('.star-rating');
        
//         // Character counter
//         if (messageField && charCount) {
//             messageField.addEventListener('input', function() {
//                 const count = this.value.length;
//                 charCount.textContent = count;
                
//                 if (count > 1000) {
//                     charCount.style.color = '#dc3545';
//                 } else if (count > 800) {
//                     charCount.style.color = '#ffc107';
//                 } else {
//                     charCount.style.color = '#6c757d';
//                 }
//             });
//         }
        
//         // Star rating functionality
//         if (starRating) {
//             const stars = starRating.querySelectorAll('.star');
//             const ratingText = document.querySelector('.rating-text');
            
//             stars.forEach((star, index) => {
//                 star.addEventListener('click', function() {
//                     const rating = 5 - index;
//                     const radioInput = document.getElementById(`star${rating}`);
//                     if (radioInput) {
//                         radioInput.checked = true;
//                     }
                    
//                     // Update rating text
//                     const ratingTexts = {
//                         5: 'Excellent! 🌟',
//                         4: 'Very Good! 👍',
//                         3: 'Good 👌',
//                         2: 'Fair 🤔',
//                         1: 'Poor 😞'
//                     };
                    
//                     if (ratingText) {
//                         ratingText.textContent = ratingTexts[rating] || 'Click to rate';
//                     }
//                 });
                
//                 // Hover effects
//                 star.addEventListener('mouseenter', function() {
//                     const rating = 5 - index;
//                     highlightStars(rating);
//                 });
//             });
            
//             starRating.addEventListener('mouseleave', function() {
//                 const checkedInput = starRating.querySelector('input:checked');
//                 if (checkedInput) {
//                     highlightStars(parseInt(checkedInput.value));
//                 } else {
//                     highlightStars(0);
//                 }
//             });
//         }
        
//         // Feedback form submission
//         if (feedbackForm) {
//             feedbackForm.addEventListener('submit', function(e) {
//                 e.preventDefault();
                
//                 // Simulate submission
//                 setTimeout(() => {
//                     const successAlert = document.querySelector('.feedback-success');
//                     if (successAlert) {
//                         successAlert.classList.remove('d-none');
//                         successAlert.scrollIntoView({ behavior: 'smooth' });
//                     }
                    
//                     // // Reset form
//                     // this.reset();
//                     // if (charCount) charCount.textContent = '0';
//                     // if (ratingText) ratingText.textContent = 'Click to rate your experience';
//                     // highlightStars(0);
//                 }, 1000);
//             });
//         }
//     }
    
//     // Highlight stars for rating
//     function highlightStars(rating) {
//         const stars = document.querySelectorAll('.star');
//         stars.forEach((star, index) => {
//             const starRating = 5 - index;
//             if (starRating <= rating) {
//                 star.classList.add('active');
//             } else {
//                 star.classList.remove('active');
//             }
//         });
//     }
    
//     // =============================================================================
//     // UTILITY FUNCTIONS
//     // =============================================================================
    
//     // Show toast notification
//     function showToast(message, type = 'info') {
//         const toast = document.createElement('div');
//         toast.className = `toast align-items-center text-white bg-${type} border-0`;
//         toast.setAttribute('role', 'alert');
//         toast.innerHTML = `
//             <div class="d-flex">
//                 <div class="toast-body">${message}</div>
//                 <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
//             </div>
//         `;
        
//         // Add to page
//         let toastContainer = document.querySelector('.toast-container');
//         if (!toastContainer) {
//             toastContainer = document.createElement('div');
//             toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
//             document.body.appendChild(toastContainer);
//         }
        
//         toastContainer.appendChild(toast);
        
//         // Initialize and show toast
//         const bsToast = new bootstrap.Toast(toast);
//         bsToast.show();
        
//         // Remove from DOM after hiding
//         toast.addEventListener('hidden.bs.toast', () => {
//             toast.remove();
//         });
//     }
    
//     // Password toggle functionality
//     function initPasswordToggle() {
//         const toggleButtons = document.querySelectorAll('#togglePassword');
        
//         toggleButtons.forEach(button => {
//             button.addEventListener('click', function() {
//                 const passwordInput = this.parentNode.querySelector('input[type="password"], input[type="text"]');
//                 const toggleIcon = this.querySelector('#toggleIcon');
                
//                 if (passwordInput && toggleIcon) {
//                     if (passwordInput.type === 'password') {
//                         passwordInput.type = 'text';
//                         toggleIcon.classList.replace('bi-eye', 'bi-eye-slash');
//                     } else {
//                         passwordInput.type = 'password';
//                         toggleIcon.classList.replace('bi-eye-slash', 'bi-eye');
//                     }
//                 }
//             });
//         });
//     }
    
//     // Smooth scrolling for anchor links
//     function initSmoothScrolling() {
//         const links = document.querySelectorAll('a[href^="#"]');
        
//         links.forEach(link => {
//             link.addEventListener('click', function(e) {
//                 const href = this.getAttribute('href');
//                 if (href === '#') return;
                
//                 const target = document.querySelector(href);
//                 if (target) {
//                     e.preventDefault();
//                     target.scrollIntoView({ behavior: 'smooth' });
//                 }
//             });
//         });
//     }
    
//     // Add loading state to buttons
//     function addButtonLoadingState() {
//         const buttons = document.querySelectorAll('.btn[type="submit"]');
        
//         buttons.forEach(button => {
//             button.addEventListener('click', function() {
//                 const spinner = this.querySelector('.spinner-border');
//                 if (spinner) {
//                     this.disabled = true;
//                     spinner.classList.remove('d-none');
                    
//                     // Re-enable after 3 seconds (demo)
//                     setTimeout(() => {
//                         this.disabled = false;
//                         spinner.classList.add('d-none');
//                     }, 3000);
//                 }
//             });
//         });
//     }
    
//     // =============================================================================
//     // GLOBAL FUNCTIONS (for template usage)
//     // =============================================================================
    
//     // Make functions available globally
//     window.regenerateContent = function() {
//         const aiForm = document.getElementById('aiSuggestionForm');
//         if (aiForm) {
//             handleAISubmission({ target: aiForm, preventDefault: () => {} });
//         }
//     };
    
//     window.saveContent = function() {
//         showToast('Content saved to favorites!', 'success');
//     };
    
//     // =============================================================================
//     // INITIALIZATION
//     // =============================================================================
    
//     // Initialize all functionality
//     initFormValidation();
//     initAISuggestions();
//     initFeedbackForm();
//     initPasswordToggle();
//     initSmoothScrolling();
//     addButtonLoadingState();
    
//     // Add subtle animations to cards
//     const cards = document.querySelectorAll('.card, .tool-card, .template-card');
//     cards.forEach(card => {
//         card.addEventListener('mouseenter', function() {
//             this.style.transform = 'translateY(-2px)';
//         });
        
//         card.addEventListener('mouseleave', function() {
//             this.style.transform = 'translateY(0)';
//         });
//     });
    
//     console.log('ParlorPal JavaScript initialized successfully! 💜');
// });

// // =============================================================================
// // ADDITIONAL UTILITY FUNCTIONS
// // =============================================================================

// // Debounce function for performance
// function debounce(func, wait) {
//     let timeout;
//     return function executedFunction(...args) {
//         const later = () => {
//             clearTimeout(timeout);
//             func(...args);
//         };
//         clearTimeout(timeout);
//         timeout = setTimeout(later, wait);
//     };
// }

// // Format text for social media
// function formatSocialText(text) {
//     return text
//         .replace(/\n/g, '\n\n')
//         .replace(/#(\w+)/g, '<span class="hashtag">#$1</span>');
// }

// // Simple animation helper
// function animateElement(element, animationClass, duration = 1000) {
//     element.classList.add(animationClass);
//     setTimeout(() => {
//         element.classList.remove(animationClass);
//     }, duration);
// }