function target_selection_onclick() {
    if (document.getElementById('Test1').checked || document.getElementById('Test2').checked) {
        document.getElementById('not_carousel').style.display = 'block';
    }
    else document.getElementById('not_carousel').style.display = 'none';

}