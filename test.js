// testing the counter object
/*

var l = 'adfslfjguvdgfohugkposv'
var s = 'doiguoeigcfvrpdfghiimb'

function counter(str){
  // define the object that will count the frequency of each letter
  var  counter_obj = {}

  // loop through each letter
  for (var i = 0; i < str.length;i++){
    if (str[i] in counter_obj){
      counter_obj[str[i]]++;
    }
    else {
      counter_obj[str[i]] = 1
    }
  }
  return counter_obj
}



function subtractLetters(s1,s2) {
// take out all the letters that are in s2 from s1

  var counterS1 = counter(s1);
  console.log(counterS1)
  var counterS2 = counter(s2);

  for (var i in counterS1){
    if(i in counterS2) {
      counterS1[i] = counterS1[i] - counterS2[i]
      if (counterS1[i] <= 0){
        delete counterS1[i];
      }
    }
  }
  console.log(counterS1)
}

subtractLetters(s,l)
*/
//working on getting it done 
// september 21st coding interview question
// create a function that imitates the flat method 

Array.prototype.flat = function(depth) {
  
  var new_array = []
  for (var i = 0; i <this.length; i++){
    if (typeof(this[i]) === 'number'){ 
      new_array.push(this[i])
    }
    else {
     
      for (var j = 0; j < this[i].length; j++) {
        
        new_array.push(this[i][j])
      }
    }
  }
  return new_array
}
var l = [1,2,3,4,5,6,[12,14,16]]

console.log(l.flat(1))

