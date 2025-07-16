// script.js

document.addEventListener('DOMContentLoaded', () => {
    const questionImageInput = document.getElementById('questionImage');
    const imagePreview = document.getElementById('image-preview');
    const imagePreviewContainer = document.getElementById('image-preview-container');
    const fileNameDisplay = document.getElementById('file-name-display');
    const uploadForm = document.getElementById('uploadForm');
    const messageBox = document.getElementById('messageBox');
    const messageText = document.getElementById('messageText');
    const messageCloseButton = document.getElementById('messageCloseButton');

    // Function to display custom messages
    function showMessage(message) {
        messageText.textContent = message;
        messageBox.classList.remove('hidden');
    }

    // Event listener for closing the message box
    messageCloseButton.addEventListener('click', () => {
        messageBox.classList.add('hidden');
    });

    // Event listener for file input change
    questionImageInput.addEventListener('change', function() {
        const file = this.files[0];

        if (file) {
            // Display file name
            fileNameDisplay.textContent = `चुनी गई फ़ाइल: ${file.name}`;

            // Check file size (e.g., limit to 5MB)
            const maxSize = 5 * 1024 * 1024; // 5MB
            if (file.size > maxSize) {
                showMessage('फ़ाइल का आकार 5MB से अधिक नहीं होना चाहिए। कृपया एक छोटी फ़ाइल चुनें।');
                this.value = ''; // Clear the input
                imagePreviewContainer.classList.add('hidden');
                fileNameDisplay.textContent = '';
                return;
            }

            // Check file type
            const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
            if (!allowedTypes.includes(file.type)) {
                showMessage('केवल JPG, PNG, GIF, या WebP छवियाँ ही अपलोड की जा सकती हैं।');
                this.value = ''; // Clear the input
                imagePreviewContainer.classList.add('hidden');
                fileNameDisplay.textContent = '';
                return;
            }

            // Read the file as a URL for preview
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreviewContainer.classList.remove('hidden');
            };
            reader.readAsDataURL(file);
        } else {
            // No file selected, hide preview and clear file name
            imagePreview.src = "#";
            imagePreviewContainer.classList.add('hidden');
            fileNameDisplay.textContent = '';
        }
    });

    // Handle form submission to show loading indicator or prevent multiple submissions
    uploadForm.addEventListener('submit', (e) => {
        // You can add a loading spinner or disable the button here
        // For now, we'll just show a simple message
        // e.preventDefault(); // Uncomment this if you want to handle submission via AJAX
        
        // Show a message that the image is being processed
        showMessage('आपकी तस्वीर संसाधित की जा रही है... कृपया प्रतीक्षा करें।');
        // Optionally disable the submit button to prevent multiple submissions
        uploadForm.querySelector('button[type="submit"]').disabled = true;
    });
});

