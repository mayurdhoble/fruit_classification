document.getElementById('classifyBtn').addEventListener('click', () => {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('uploadedImage').src = e.target.result;
            document.getElementById('uploadedImage').style.display = 'block';

            // Send image to backend
            fetch('/classify', {
                method: 'POST',
                body: JSON.stringify({ image: e.target.result }),
                headers: { 'Content-Type': 'application/json' }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('classificationResult').textContent = 'Fruit in image is ' + data.label;
                document.getElementById('accuracy').textContent = 'With accuracy of ' + data.accuracy + '%';
            });
        };
        reader.readAsDataURL(file);
    } else {
        alert('Please upload an image file.');
    }
});
