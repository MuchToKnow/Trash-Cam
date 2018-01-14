function map(jsonObjectArray) {
    var map = new Object();
    var c = "compost";
    var r = "recycle";
    var t = "trash";
    var a = "all";
    map["Food"] = c;
    map["Fruit"] = c;
    map["Vegetable"] = c;
    map["Plastic"] = r;
    map["Metal"] = r;
    map["Glass"] = r;
    map["Carton"] = r;
    map["Cup"] = r;
    map["Bottle"] = r;
    map["Paper"] = r;
    map["Bag"] = t;
    map["Styrofoam"] = t;
    
    
    for (int i = 0; i < jsonObjectArray.length; i++) {
        var object = jsonObjectArray[i].name;
        if (object in map) {
            return map[object];
        }
    }
    
    return a;
}
