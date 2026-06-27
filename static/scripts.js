async function predict() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select an image first');
        return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        document.getElementById('preview').src = e.target.result;
        document.getElementById('preview-box').style.display = 'block';
    };
    reader.readAsDataURL(file);

    // Send to API
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();

    document.getElementById('label').textContent = result.label;
    document.getElementById('confidence').textContent = `Confidence: ${result.confidence}%`;
    document.getElementById('result').style.display = 'block';
}