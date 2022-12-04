const display = document.getElementById("display");
var oldNumbers = []
var signals = []


function num(n) {
  display.value += n;
}


function operation(o) {
  var number = parseFloat(display.value)
  oldNumbers.push(number)
  if (o !== 0) {
  signals.push(o)
  }
  display.value = ""
}


function toggle() {
  display.value = -display.value
}


function c() {
  if (display.value !== "") {
    display.value = ""
  } else {
    if (display.length > 0) {
    display.value = oldNumbers[oldNumbers.length - 1]
    oldNumbers.pop()
    signals.pop()
    }
  }
}

function ac() {
  oldNumbers.length = 0
  signals.length = 0
  display.value = ""
}


function equal() {
  operation(0)
  while (oldNumbers.length >= 2) {
    switch(signals[0]) {
      case 'subtraction':
        var total = oldNumbers[0] - oldNumbers[1]
        console.log(total)
        oldNumbers.shift()
        oldNumbers.shift()
        oldNumbers.unshift(total)
        signals.shift()
        break;
      case 'sum':
        var total = oldNumbers[0] + oldNumbers[1]
        console.log(total)
        oldNumbers.shift()
        oldNumbers.shift()
        oldNumbers.unshift(total)
        signals.shift()
        break;
      case 'multiplication':
        var total = oldNumbers[0] * oldNumbers[1]
        console.log(total)
        oldNumbers.shift()
        oldNumbers.shift()
        oldNumbers.unshift(total)
        signals.shift()
        break;
      case 'division':
        var total = oldNumbers[0] / oldNumbers[1]
        console.log(total)
        oldNumbers.shift()
        oldNumbers.shift()
        oldNumbers.unshift(total)
        signals.shift()
        break;
    }
  }
  display.value = oldNumbers[0] 
  oldNumbers.length = 0
}