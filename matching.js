function map(text) {
    var map = new Object();
    var c = "compost";
    var r = "recycle";
    var t = "trash";
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
    
    var objects = text.split(",");
    
    for (int i = 0; i < objects.length; i++) {
        if (objects(i) in map) {
            return map[objects(i)];
        }
    }
}
