// Code.gs — entry for HTML web app
function doGet(e) {
  return HtmlService.createTemplateFromFile('index')
                    .evaluate()
                    .setTitle('Clinical Assistant — Basic SPA')
                    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// include helper to load html file into index
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}
