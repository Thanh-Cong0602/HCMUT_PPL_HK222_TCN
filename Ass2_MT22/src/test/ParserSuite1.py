import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test0(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            arr: array[2,3,4] of integer = {55,66,77};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 301))
    def test1(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            arr,arr1: array[5,6,7] of integer = {123,1231,23};
        }"""
        expect = "Error on line 2 col 61: ;"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test2(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            arr: array[2,3,4] of integer = {}, {};
        }"""
        expect = "Error on line 2 col 45: ,"
        self.assertTrue(TestParser.test(input, expect, 202))  
    def test3(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            delta: integer = fact(3);
            inc(x,delta);
            printint(x);
            return abc*func(2,3);
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203)) 
    def test4(self):
        """Simple program: int main() {} """
        input = """

        main: function void () {
                while (x == 1) {
              if(n == 0) return 1;
              else return n*fact(n - 1);
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test5(self):
        """Simple program: int main() {} """
        input = """
        /* comment */
        main: function void () {
            do {
              if(n == 0) return 1;
              else return n*fact(n-1);
             }
            while (x == 1);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test6(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            for (x[1] = 2, x == 1, x + 1) {
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            /* this is a block comment */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        input = """
                a : boolean = true;
                add: function void(i: float) {
                    return i;
                }
                inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                    n = n + delta + hallo;
                    n = n - delta - hallo;
                    n = n * delta * hallo;
                    /* multiple
                        line
                        comment
                    */
                    n = n / delta / hallo;
                    n = true;
                    n = n % 1 + hallo - 1+2;
                    n = n && delta && hallo;
                    n = n || delta || hallo;
                    n = n :: n;
                    n = n + add(delta);
                    n = a[1, a[1, a[1,2]]]; // n[1,2] = 2 => n = a[1,2];
                    return n;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            if (true) {
            return 1;
            }
            return {1,2,3};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        """Simple program: int main() {} """
        input = """
        
            if (true) {
            return 1;
            }
            return {1,2,3};
        
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test11(self):
        input = """
            x,y,z: integer = 3, 4, 6;
            fact:function integer(n:integer)
            {
                if((n==0)||(n==1)||(n==2))return 1;
                result:integer=1;
                a:integer=1;
                b:integer=1;
                while(n>2)
                {
                    result=a+b;
                    a=b;
                    b=result;
                    n=n-1;
                }
                return result;
            }
            fact: function integer (n: integer) {
                if (n == 0) return 1;
                else return n * fact(n - 1);
            }
            inc: function void(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = fact(3);
                inc(x, delta);
                printInteger(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        """Simple program: int main() {} """
        input = """
            main: function void () {
            foo({1,2,3,4});
            return {1,2,3};
        
        
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_multi_function_declaration_and_bodies(self):
        input = """foo: function integer(x: integer) {
                z: integer;
                z = x + 1;
                return z;
            }
            bar: function float(y: float) {
                z: float;
                z = y * 2.0;
                return z;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        input = "foo: function void (x: integer[][]) {}"
        expect = "Error on line 1 col 30: ["
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        """Simple program: int main() {} """
        input = """
        a: integer;
        main: function void () {
            for(a=1,true,a+1){
                a = a + 1;
            }
        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self):
        """Simple program: int main() {} """
        input = """
        a: integer;
        main: function void () {
            for(a=1,true,a+1){
                a = a + 1;
                break;
            }
            do {
                continue;
                a = "1234";
                a = a::a;
            }
            while(true);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        main: function void() {
            foo();
            bar();
            baz();
        }
        foo: function void() {
            x = y + z;
        }
        bar: function void() {
            y = x + z;
        }
        baz: function void() {
            z = x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """main: function void() {
            
            for (i=0, i<10, i + 1) {
                printInteger(max);
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        input = """
            fibo: function integer(n: integer){
                return n;
            }
            main: function void() {
            
            for (i=0, i<10, i + 1) {
                printInteger(max);
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        input = """
            fibo: function integer(n: integer){
                return fibo(n-1) + fibo(n-2);
            }
            main: function void() {
            
            for (i=0, i<10, i + 1) {
                printInteger(max);
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_error_program_string(self):
        input = """x: boolean = true;
        y: boolean = false;
        z: boolean = (x == y);
        main: function void() {
            if (x) {
                print("x is true");
            } else {
                print("x is false");
            }
            if (y) {
                print("y is true");
            } else {
                print("y is false");
            }
            if (z) {
                print("z is true");
            } else {
                print("z is false");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        input = """
            main: function void() {
            
            if ((a == b) || (a == 3)) {
                readString();
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        input = """
            main: function void() {
            
                a: integer = {1234};
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))

    def test24(self):
        input = """
            main: function void() {
            
                foo({1,2,3,4});
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))

    def test25(self):
        input = """main: function void() {
        do {
        if ( (max % n1 == 0) && (max % n2 == 0) )
            {
                print("LCM = ");
                printInteger(max);
                break;
            }
        else max = max +1;
        } while (true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 225))

    def test27(self):
        input = """main: function void() {
        while (a[1] == 1) a = a + 1;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        input = """main: function void() {
        while (a[1] == 1) {}
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """
        delta: integer = fact({1,2,3,4});
        a: integer = 5;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """
        delta: integer = fact({{1234}});
        a: integer = 5;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))

    def test31(self):
        input = """
        delta: integer = fact({{"1234"}});
        a: integer = 5;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))

    def test33(self):
        input = """main: function void() {
        while (a[1] == 1) if (a == b) readInteger();
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))

    def test34(self):
        input = """main: function void() {
        x:integer = foo(foo(1234));
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))

    def test35(self):
        input = """main: function void() {
        x:integer = foo(foo(1234));
        for (x=1,1,x+2) break;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        input = """main: function void() {
        foo({123},{134});
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        input = """main: function void() {
        a,b : integer = foo({123},{134}), foo({123},{134});
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = """main: function void() {
            for (a = 1, a == 1, a = a + 1) {
                a = 1;
                break;
            }
        }"""
        expect = """Error on line 2 col 34: ="""
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """main: function array [2,3] of integer (n: integer) {
            x: integer = 65;
            y: array [2] of integer = {2, 4};
            printInt(1244123);
            writeFloat(1.23);
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """main: function void() {
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 240))

    def test41(self):
        input = """main: function void() {
                a: string = \"1234\";
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """main: function void() {
                x: array [2,3] of boolean = {{true, false, true}, {false, true, false}};
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """main: function void() {
                x: array [2,3] of float = {{1.2, -2, 3.5e2}, {-2_3.5e10, -100.1, 2.3434}};
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """
        main: function void()[]
        """
        expect = """Error on line 2 col 29: ["""
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """
        main: function vod(){}
        """
        expect = """Error on line 2 col 23: vod"""
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """
        main: function void(){
        
            x = a + b + c + 12;
            return \" hello,hi\";
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """
        main: function void(){
            for(x = y + z, x < z, x + y) {
                return x + y + z * 3;
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """
        main: function void(){
            a: array[3,4] = {1,2,3,4,5};
            return a[3];
        }
        """
        expect = """Error on line 3 col 26: ="""
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            arr: array[2,3,4] of integer = {123,1231,23};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test51(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            arr,arr1: array[2,3,4] of integer = {123,1231,23};
        }"""
        expect = "Error on line 2 col 61: ;"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test52(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            arr: array[2,3,4] of integer = {}, {};
        }"""
        expect = "Error on line 2 col 45: ,"
        self.assertTrue(TestParser.test(input, expect, 252))  
    def test53(self):
        """Simple program: int main() {} """
        input = """main: function void () {
            delta: integer = fact(3);
            inc(x,delta);
            printint(x);
            return abc*func(2,3);
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253)) 
    def test54(self):
        """Simple program: int main() {} """
        input = """

        main: function void () {
                while (x == 1) {
              if(n == 0) return 1;
              else return n*fact(n - 1);
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test55(self):
        """Simple program: int main() {} """
        input = """
        /* comment */
        main: function void () {
            do {
              if(n == 0) return 1;
              else return n*fact(n-1);
             }
            while (x == 1);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            for (x[1] = 2, x == 1, x + 1) {
                x = 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            /* this is a block comment */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            if (true) {
            return 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            if (true) {
            return 1;
            }
            return {1,2,3};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        """Simple program: int main() {} """
        input = """
        
            if (true) {
            return 1;
            }
            return {1,2,3};
        
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test61(self):
        """Simple program: int main() {} """
        input = """
            main: function void () {
            foo({1,2,3,4});
            return {1,2,3};
        }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        """Simple program: int main() {} """
        input = """
            main: function void () {
            foo({1,2,3,4});
            return {1,2,3};
        
        
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test63(self):
        """Simple program: int main() {} """
        input = """
            main: function void () {
                a = {1,2,3};
            }
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test64(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            for(a=1,true,a+1){
                a = a + 1;
            }
        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        """Simple program: int main() {} """
        input = """
        a: integer;
        main: function void () {
            for(a=1,true,a+1){
                a = a + 1;
            }
        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        """Simple program: int main() {} """
        input = """
        a: integer;
        main: function void () {
            for(a=1,true,a+1){
                a = a + 1;
                break;
            }
            do {
                continue;
                a = "1234";
                a = a::a;
            }
            while(true);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        """Simple program: int main() {} """
        input = """
        
        main: function void () {
            a,b,c,, :integer = 1,2,3;
        }
        """
        expect = "Error on line 4 col 18: ,"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """main: function void() {
            
            for (i=0, i<10, i + 1) {
                printInteger(max);
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_parser69(self):
        input = """foo: function integer () {
                            a = 5;
                            b = 3 * 5;
                            if (3 > 5) c = 123.123;
                            if (true && false) {
                                d = a + b;
                            } else {
                                d = a;
                            }
                            for (i = 1, i < 10, i + 1) {
                                writeInt(i);
                            }
                            while (a >= b) {
                                a = a - b;
                            }
                            do {
                                a = a + 1;
                            } while (a < 100);
                            break;
                            continue;
                            return a + b;
                            foo(2 + x, 4.0 / y);
                            go();
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """
            fibo: function integer(n: integer){
                return fibo(n-1) + fibo(n-2);
            }
            main: function void() {
            
            for (i=0, i<10, i + 1) {
                printInteger(max);
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 270))

    def test71(self):
        input = """
            fibo: function integer(n: integer){
                return fibo(n-1) + fibo(n-2);
            }
            main: function void() {
            
            for (i=0, i<10, i + 1) {
                printInteger(max);
                fibo(3);
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))

    def test72(self):
        input = """
            main: function void() {
            
            if ((a == b) || (a == 3)) {
                readString();
            }
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))

    def test73(self):
        input = """
            main: function void() {
            
                a: integer = {1234};
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))

    def test74(self):
        input = """
            main: function void() {
            
                foo({1,2,3,4});
            
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))

    def test75(self):
        input = """
            main:function void(){
                printString("Hay nhap tuoi cua ban");
                a:integer=readInteger();
                printString("So tuoi cua ban la: ");
                printInteger(a);
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test76(self):
        input = """foo: function float (a: integer, b: float) inherit bar {
                            return a + b;
                        }
                        main: function integer () {
                            x: integer;
                            y: integer;
                            z: integer;
                            t: integer;
                            u: integer;
                            v: integer;
                            x = 10;
                            y = 20;
                            z = x + y;
                            t = z * 2;
                            u = t / 4;
                            v = u - 5;
                            writeInt(v);

                            return 0;
                        }
                        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test77(self):
        input = """main: function void() {
        while (a[1] == 1) a = a + 1;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 277))

    def test78(self):
        input = """main: function void() {
        while (a[1] == 1) {}
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))

    def test79(self):
        input = """
        delta: integer = fact({1,2,3,4});
        a: integer = 5;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 279))

    def test80(self):
        input = """
            x:boolean=!!!true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))


    def test81(self):
        input = """
        delta: integer = fact({{"1234"}});
        a: integer = 5;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281))

    def test83(self):
        input = """main: function void() {
        while (a[1] == 1) if (a == b) readInteger();
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 283))

    def test84(self):
        input = """main: function void() {
        x:integer = foo(foo(1234));
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 284))

    def test85(self):
        input = """main: function void() {
        x:integer = foo(foo(1234));
        for (x=1,1,x+2) break;
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 285))

    def test86(self):
        input = """main: function void() {
        foo({123},{134});
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 286))

    def test87(self):
        input = """main: function void() {
        a,b : integer = foo({123},{134}), foo({123},{134});
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287))

    def test88(self):
        input = """main: function void() {
            for (a = 1, a == 1, a = a + 1) {
                a = 1;
                break;
            }
        }"""
        expect = """Error on line 2 col 34: ="""
        self.assertTrue(TestParser.test(input, expect, 288))

    def test89(self):
        input = """main: function array [2,3] of integer (n: integer) {
            x: integer = 65;
            y: array [2] of integer = {2, 4};
            printInt(1244123);
            writeFloat(1.23);
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 289))

    def test90(self):
        input = """main: function void() {
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 290))

    
    def test_call_function_86(self):
        input = """main:function void(){
        if (true)
            if (true)
                if (true)
                    if (true)
                        if (true)
                            writeln("TRUE");
                else writeln("FALSE");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test92(self):
        input = """main: function void() {
                x: array [2,3] of boolean = {{true, false, true}, {false, true, false}};
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 292))

    def test93(self):
        input = """main: function void() {
                x: array [2,3] of float = {{1.2, -2, 3.5e2}, {-2_3.5e10, -100.1, 2.3434}};
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 293))

    def test94(self):
        input = """
        main: function void()[]
        """
        expect = """Error on line 2 col 29: ["""
        self.assertTrue(TestParser.test(input, expect, 294))

    def test95(self):
        input = """
        main: function vod(){}
        """
        expect = """Error on line 2 col 23: vod"""
        self.assertTrue(TestParser.test(input, expect, 295))

    def test96(self):
        input = """
        main: function void(){
        
            x = a + b + c + 12;
            return \" hello,hi\";
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 296))

    def test97(self):
        input = """
        main: function void(){
            for(x = y + z, x < z, x + y) {
                return x + y + z * 3;
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 297))

    def test98(self):
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        input = """
        main: function void() {
        a:integer;
        a = -5*10/2 + 10;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 299))
        
    
    def test26(self):
        input = """main: function void() {
        while(a == {1,2,3,4}) {
                n = n + 1;
            }
        }
        """
        expect = """Error on line 2 col 19: {"""
        self.assertTrue(TestParser.test(input, expect, 226))
        
    
    
    def test32(self):
        input = """foo: function float (a: integer, b: float) inherit bar {
                            a = 5;
                            b = 3 * 5;
                            if (3 > 5) c = 123.123;
                            if( true && false) {d = a + b;} else {d = a;}
                            for(i = 1, i < 10, i + 1) {writeInt(i);}
                            while(a>= b) a = a - b;
                            do {a = a + 1;} while (a < 100);
                            break;
                            continue;
                            return a + b;
                            foo(2 + x, 4.0/y);
                            go();
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

        # Test function declaration
    def test82(self):
        input = "foo: function integer (x: integer);"
        expect = "Error on line 1 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 282))
        
    # def test76(self):
    #     input = """main: function void() {printString("\\n \\t \\' \\r \\" ");}
    #     """
    #     expect = """successfull"""
    #     self.assertTrue(TestParser.test(input, expect, 276)) ??????
        