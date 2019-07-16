
var leftNavLi = document.getElementsByClassName('leftNavLi');

// determine aValue exists in arr，return location or -1.
function arrIndexOf(arr, aValue){
    for(var i=0;i<arr.length;i++){
        if(arr[i] === aValue){
            return i;
        }
    }

    return -1;
}

function addClass(obj, className) {
    if (obj.className === "") {
        obj.className = className;
    } else {
        var arr = obj.className.split(" ");
        if (arrIndexOf(arr, className) === -1) {
            obj.className += " " + className;
        }
    }
}

function removeClass(obj, sClassName) {
    var arr = obj.className.split(" ");

    if (arrIndexOf(arr, sClassName) !== -1) {
        arr.splice(arrIndexOf(arr, sClassName), 1);
        obj.className = arr.join(" ");
    }
}

for (var i = 0; i < leftNavLi.length; i++) {

    ( function (n) {

        leftNavLi[n].onclick = function () {
            for (var j = 0; j < leftNavLi.length; j++) {
                removeClass(leftNavLi[j].firstElementChild, 'active');
            }

            addClass(this.firstElementChild, 'active');
            console.log(this.firstElementChild.className);
        }
    }(i))

}