function findIndexOfSubArray(arr){

    const x = arr.length

    // identify the start of sub-array
    let start = 0
    while(start < x - 1 && arr[start] <= arr[start + 1]){
        start ++
    }
    // edgecase 
    if (start === x - 1){
        return [0,0]
    }

    // identify the end of the sub-array
    let end = x -1
    while(end > 0  && arr[end] > arr[end - 1]) {
        end--
    }

    // find min and max val in sub-array
    let min = arr[start]
    let max = arr[start]
    for (let i = start + 1; i <= end; i++ ){
        if(arr[i] < arr[start]){
            min = arr[i]
        }
        else{
            max = arr[i]
        }
    }

    while (start > 0 && arr[start - 1] > min) {
        start--;
    }

    while (end < x - 1 && arr[end + 1] < max) {
        end++;
    }

    return [start, end];
}