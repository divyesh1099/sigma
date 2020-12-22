document.addEventListener("DOMContentLoaded", function (event) {
    console.log("This is Divyesh");
    let sc=document.createElement('script')
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/jwd4eruiktd917w3cx8av8sv7x9x4fj35vb3al8chl6syj43/tinymce/5/tinymce.min.js');
    document.head.appendChild(sc);
    sc.onload = ()=>{
        tinymce.init({
        selector: 'textarea',
        plugins: 'textcolor save link image media preview codesample contextmenu table code lists fullscreen  insertdatetime  nonbreaking contextmenu directionality searchreplace wordcount visualblocks visualchars code fullscreen autolink lists  charmap print  hr anchor pagebreak',
        toolbar1:'fullscreen preview bold italic underline | fontselect, fontsizeselect  | forecolor backcolor | alignleft alignright | aligncenter alignjustify | indent outdent | bullist numlist table | link image media | codesample |',
        toolbar2:'visualblocks visualchars | charmap hr pagebreak nonbreaking anchor |  code',
        toolbar_mode: 'floating',
        tinycomments_mode: 'embedded',
        tinycomments_author: 'Author name'
      });
    }
    
});