import Glibc
import Foundation

public struct StderrOutputStream: OutputStreamType {
    public mutating func write(string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

let n = Int(readLine()!)! // the number of temperatures to analyse
let temps = (readLine()!).characters.split{$0 == " "}.map(String.init).map{Int($0)!} // the n temperatures expressed as integers ranging from -273 to 5526

var res: Int = 0
var tmp: Int = 5527

for v in temps {
    if (abs(v) < tmp) || (abs(v) == tmp && v > 0) {
        res = v
        tmp = abs(v)
    }
}

print("\(res)")