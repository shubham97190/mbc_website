function getUrlParam(paramName) {
    var reParam = new RegExp('(?:[\?&]|&amp;)' + paramName + '=([^&]+)', 'i') ;
    var match = window.location.search.match(reParam) ;

    return (match && match.length > 1) ? match[1] : '' ;
}

function setImage(inputname,imageval,imagename){
    window.opener.ajax_select_image(inputname, imageval,imagename);
    window.close()
}

function setImageCKE(filename) {
    var funcNum = getUrlParam('CKEditorFuncNum');
    window.opener.CKEDITOR.tools.callFunction(funcNum,filename);
    window.close();
}

function setFile(inputname,fileval,filename){
    window.opener.ajax_select_image(inputname, fileval,filename);
    window.close()
}

function setFileCKE(filename) {
    var funcNum = getUrlParam('CKEditorFuncNum');
    window.opener.CKEDITOR.tools.callFunction(funcNum,filename);
    window.close()
}