async function analyze() {
    const resume = document.getElementById('resume').value;
    const job = document.getElementById('job').value;
    const resultDiv = document.getElementById('result');
    const resultContainer = document.getElementById('result-container');
    const loader = document.getElementById('loader');
    const btnText = document.getElementById('btn-text');

    loader.classList.remove('hidden');
    btnText.classList.add('hidden');

    try {
        const response = await fetch('/resume_analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ resume_text: resume, job_description: job })
        });

        const data = await response.json();

        resultDiv.textContent = JSON.stringify(data, null, 2);
        resultContainer.classList.remove('hidden');
    } catch (error) {
        resultDiv.textContent = "Error: " + error;
        resultContainer.classList.remove('hidden');
    } finally {
        loader.classList.add('hidden');
        btnText.classList.remove('hidden');
    }
}