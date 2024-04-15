fetch('./data.json')
    .then((response) => response.json())
    .then((json) => {
        console.log(json); // This will log the fetched JSON data
        addDatatoTable(json); // Pass the fetched data to the function
    })
    .catch((error) => console.error('Error fetching data:', error));

const addDatatoTable = (data) => {
    const tbl = document.getElementById('data');

    data.forEach(item => {
        const row = document.createElement('tr');

        const judulCell = document.createElement('td');
        judulCell.textContent = item.judul;
        row.appendChild(judulCell);

        const taanggalCell = document.createElement('td');
        taanggalCell.textContent = item.tanggal;
        row.appendChild(taanggalCell);

        const menitCell = document.createElement('td');
        menitCell.textContent = item.waktu_rilis.split(" - ")[0];
        row.appendChild(menitCell);

        const waktuScrapping = document.createElement('td');
        waktuScrapping.textContent = item.waktu_scrapping;
        row.appendChild(waktuScrapping);

        tbl.appendChild(row);

    });
};