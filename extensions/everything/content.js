chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
    	console.log("received")
		// Communicate with background.js
		chrome.runtime.sendMessage({
			"message": "change_elements"
		});
    }
  }
);

