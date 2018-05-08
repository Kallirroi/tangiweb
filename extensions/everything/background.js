chrome.webNavigation.onCompleted.addListener(function(details) {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    console.log('sent query')
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
  });
})
  
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "change_elements" ) {
    chrome.tabs.insertCSS({
      file: "addedStyles.css"
    });
    }
  }
);