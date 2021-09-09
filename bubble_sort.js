


function bbubble(arr){
  var indexing_length = arr.length -1;
  
  var sorted = false

  while(!sorted){
    
    sorted = true;

    for (var i = 0; i < indexing_length; i++){
      
      if (arr[i] > arr[i + 1]) {
       
        sorted = false;
        
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        console.log('sorting')
      }
    }
  
  }
  console.log(arr)
}
var arra = [0,8,7,6,5,4,3,2,1]


console.log(bbubble(arra))