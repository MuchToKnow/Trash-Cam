module.exports.matching=function(jsonObjectArray, call2, response) {
    var map = new Object();
    var c = "compost";
    var r = "recycle";
    var t = "trash";
    var a = "all";
    map["Fruit"] = 1;
    map["Vegetable"] = 1;
    map["Flora"] = 1;
    map["Plastic"] = 2;
    map["Metal"] = 2;
    map["Glass"] = 2;
    map["Carton"] = 2;
    map["Cardboard"] = 2;
    map["Box"] = 2;
    map["Cup"] = 2;
    map["Bottle"] = 2;
    map["Diary"] = 2;
    map["Paper"] = 2;
    map["Beer Bottle"] = 2;
    map["Drink"] = 2;
    map["Electronics"] = 3;
    map["Computer Hardware"] = 3;
    map["Hardware"] = 3;
    map["Bag"] = 3;
    map["Styrofoam"] = 3;
    map["Plastic Wrap"] = 3;
    map["Plastic Bag"] = 3;
    
    console.log("matching...");
    console.log(jsonObjectArray.Labels.length);
    for (var i = 0; i < jsonObjectArray.Labels.length; i++) {
        var object = jsonObjectArray.Labels[i].Name;
        if (object in map) {
            console.log(map[object]);
            call2(map[object], response);
            return 0;
            //return(map[object]);
        }
    }
    console.log(0);
    call2(0, response);
    return(0);
}