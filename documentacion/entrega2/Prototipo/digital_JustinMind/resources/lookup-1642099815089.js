(function(window, undefined) {
  var dictionary = {
    "2db1cdf6-13a2-4c52-b576-ccdaa4f3b0cf": "LogIn",
    "6dbc9c0a-e4dd-4d5e-97df-c6df8b3b1334": "EscribirBlog",
    "a44a2dd1-aeb7-4f2f-ba95-81ced7122c97": "RecetaConcreta",
    "2a7f71e8-bd35-43b1-981e-7e9482dc1b40": "ProductoConcreto",
    "77337877-165b-4b43-a8cd-ada8b9bebee6": "BlogConcreto",
    "bee53a27-20c5-4c3a-b800-a497a41f9347": "Blogs",
    "577c9c8c-8b93-423f-90ba-5df6cb83262e": "Busqueda",
    "97f86c1e-03c7-49c3-a1a4-4ffa224889cc": "Productos",
    "d510f765-f0ca-4474-bb5c-70a770955ea4": "Recetas",
    "d12245cc-1680-458d-89dd-4f0d7fb22724": "Home",
    "3ba1ac15-2f73-41d4-bcbe-00d7f2abf9c4": "BusquedaPalabras",
    "35d02a46-167e-4fe6-9d00-e4380227d581": "SignIn",
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