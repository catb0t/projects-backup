const worker = txt=>
  txt.split('').reduce(({floor, basement}, x, i)=> {
    if (x === '(')
      return {floor: floor + 1, basement}
    else if (basement === null && floor === 0)
      return {floor: floor - 1, basement: i}
    else
      return {floor: floor - 1, basement}
  }, {floor: 0, basement: null})

let {floor, basement} = worker('((((())(())(((()))((')
console.log(floor)    //=> 6
console.log(basement) //=> null; never reaches basement