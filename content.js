chrome.runtime.sendMessage({
    'title': document.title,
    'url': window.location.href,
    'summary':document.getElementsByClassName('vkIF2 public-DraftStyleDefault-ltr')[0].innerHTML
});