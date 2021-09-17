/*
So far this passes like 5 out of 15 tests

*/

function commonChild(s1, s2) {
  // Write your code here
  var result = 0
  // check s1 against s2:
  for (var i = 0; i < s1.length; i++){
      var childString = ''
      // if we find a match
      if (s2.indexOf(s1[i]) != -1){
          console.log('match:', s1[i])
          childString += s1[i]
          // the remaining string is are the rest of the letters after that first 
          // letter match
          var remainingString = s2.slice(s2.indexOf(s1[i]) + 1)
         
          
          // for each character after the one you just checked(the one that matched)
          //  check if that character is in the remaining string
          
          for (var k = i + 1; k < s1.length; k++){      
              if (remainingString.indexOf(s1[k]) != -1){
               
                childString += s1[k]
                
      remainingString = remainingString.slice(remainingString.indexOf(s1[k]) + 1)
                  
              }
          }
               
      }
      console.log('childString:', childString)
  result = Math.max(result, childString.length)   
  } 
  
  // check s2 agains s1

return result
}