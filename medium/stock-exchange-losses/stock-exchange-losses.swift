import Glibc

public struct StderrOutputStream: OutputStreamType {
    public mutating func write(string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

let n = Int(readLine()!)!
var tab = [Int]()
for i in ((readLine()!).characters.split{$0 == " "}.map(String.init)) {
    let v = Int(i)!
    tab.append(v)
}

// Write an action using print("message...")
// To debug: debugPrint("Debug messages...", toStream: &errStream)

var res = [0]
var vh:Int? = nil

for va in tab {
    if vh != nil && vh > va {
        res.append(va - vh!)
    }
    if vh == nil || vh < va {
        vh = va
    }
}

// Swift 2 list.minElement() vs Swift3 list.min()
print(res.minElement()!)