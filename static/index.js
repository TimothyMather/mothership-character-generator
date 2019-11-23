function generateCharacter() {
    console.log('generated')
    fetch('http://localhost:5000/generate', {
        method: 'GET',
    })
    .then(response => response.blob())
    .then(blob => {
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = "character_sheet.pdf";
        document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
        a.click();    
        a.remove();
    })
}
