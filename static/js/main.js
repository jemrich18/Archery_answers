// ===== TAB SWITCHING =====
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        // Update buttons
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Update panels
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
        document.getElementById(btn.dataset.tab).classList.add('active');
    });
});

// ===== ARROW SPEED CALCULATOR =====
function calculateSpeed() {
    const ibo = parseFloat(document.getElementById('ibo-speed').value);
    const drawLength = parseFloat(document.getElementById('draw-length').value);
    const drawWeight = parseFloat(document.getElementById('draw-weight').value);
    const arrowWeight = parseFloat(document.getElementById('arrow-weight').value);

    if (!ibo || !drawLength || !drawWeight || !arrowWeight) {
        alert('Please fill in all fields.');
        return;
    }

    // Speed deductions from IBO
    let speed = ibo;
    speed -= (30 - drawLength) * 10;           // 10 FPS per inch under 30
    speed -= (70 - drawWeight) * 1.75;          // ~17.5 FPS per 10 lbs under 70
    speed -= ((arrowWeight - 350) / 5) * 1.5;   // 1.5 FPS per 5gr over 350
    speed = Math.max(speed, 0);

    // KE = (mv^2) / 450240
    const ke = (arrowWeight * Math.pow(speed, 2)) / 450240;

    // Momentum = (mv) / 225120
    const momentum = (arrowWeight * speed) / 225120;

    // Display results
    document.getElementById('result-speed').textContent = speed.toFixed(1);
    document.getElementById('result-ke').textContent = ke.toFixed(1);
    document.getElementById('result-momentum').textContent = momentum.toFixed(2);
    document.getElementById('speed-results').classList.add('show');

    // Rate animals
    rateAnimals(ke, momentum);
}

// ===== KE & MOMENTUM CALCULATOR =====
function calculateKE() {
    const arrowWeight = parseFloat(document.getElementById('ke-arrow-weight').value);
    const speed = parseFloat(document.getElementById('ke-arrow-speed').value);

    if (!arrowWeight || !speed) {
        alert('Please fill in all fields.');
        return;
    }

    const ke = (arrowWeight * Math.pow(speed, 2)) / 450240;
    const momentum = (arrowWeight * speed) / 225120;

    document.getElementById('ke-result-ke').textContent = ke.toFixed(1);
    document.getElementById('ke-result-momentum').textContent = momentum.toFixed(2);
    document.getElementById('ke-results').classList.add('show');
}

// ===== ANIMAL RATING LOGIC =====
function rateAnimals(ke, momentum) {
    document.querySelectorAll('.animal-row').forEach(row => {
        const minKE = parseFloat(row.dataset.ke);
        const minMomentum = parseFloat(row.dataset.momentum);
        const badge = row.querySelector('.animal-badge');

        const kePass = ke >= minKE;
        const momPass = momentum >= minMomentum;

        // Remove old classes
        badge.classList.remove('badge-pass', 'badge-marginal', 'badge-fail');

        if (kePass && momPass) {
            badge.textContent = 'Pass';
            badge.classList.add('badge-pass');
        } else if (kePass || momPass) {
            badge.textContent = 'Marginal';
            badge.classList.add('badge-marginal');
        } else {
            badge.textContent = 'Insufficient';
            badge.classList.add('badge-fail');
        }
    });
}