// testing the counter object


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

