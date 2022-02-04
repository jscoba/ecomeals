(function(window, undefined) {
  var dictionary = {
    "64f54293-93b3-4ab9-b3d1-1c03ddbfb973": "Info producto",
    "d0d58821-2dea-407f-88fc-904ca0211595": "Buscar",
    "3162f65d-63a3-43f4-9667-81f9b7b8f57b": "Info receta",
    "60468cf8-0681-4b68-a7c5-23d8981e6ba0": "Mis Recetas",
    "ac0e0881-8637-41fd-8173-595a4d4d9427": "Scan producto",
    "d12245cc-1680-458d-89dd-4f0d7fb22724": "Mis Productos",
    "f39803f7-df02-4169-93eb-7547fb8c961a": "Template 1",
    "bb8abf58-f55e-472d-af05-a7d1bb0cc014": "default"
  };

  var uriRE = /^(\/#)?(screens|templates|masters|scenarios)\/(.*)(\.html)?/;
  window.lookUpURL = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, url;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      url = folder + "/" + canvas;
    }
    return url;
  };

  window.lookUpName = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, canvasName;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      canvasName = dictionary[canvas];
    }
    return canvasName;
  };
})(window);