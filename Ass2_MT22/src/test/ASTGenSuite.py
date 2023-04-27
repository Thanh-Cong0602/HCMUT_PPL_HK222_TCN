import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_more_complex_program_0(self):
        input = """
            main: function void() {
            
                foo({1,2,3,4});
            
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_more_complex_program_1(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_more_complex_program_2(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        
        expect = """Program([
\tVarDecl(x, IntegerType, IntegerLit(1))
\tVarDecl(y, IntegerType, IntegerLit(2))
\tVarDecl(z, IntegerType, IntegerLit(3))
\tVarDecl(a, FloatType)
\tVarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_more_complex_program_3(self):
        """Simple program"""
        input = """
        a,b,c: integer
        main: function void () {
            x: float = 12.12e235;
            y: float = .e1703;
            z: integer = 182005;
            input = arr[5];
            }"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.212e+236)), VarDecl(y, FloatType, FloatLit(0.0)), VarDecl(z, IntegerType, IntegerLit(182005)), AssignStmt(Id(input), ArrayCell(arr, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program_4(self):
        """More complex program"""
        input = """main: function void () {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test_more_complex_program_5(self):
        """More complex program"""
        input = """

       foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
     printInteger(4);
}
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
     
    def test_more_complex_program_6(self):
        input = """x,y: boolean = (2 == 3+4), a == "abc";"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(==, IntegerLit(2), BinExpr(+, IntegerLit(3), IntegerLit(4))))
	VarDecl(y, BooleanType, BinExpr(==, Id(a), StringLit(abc)))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
       
    def test_more_complex_program_7(self):
        input = """x, y: array [3] of integer = {1+2,2+3,3+4}, {2*1,3*2,4*3};"""
        expect = """Program([
	VarDecl(x, ArrayType([3], IntegerType), ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(2), IntegerLit(3)), BinExpr(+, IntegerLit(3), IntegerLit(4))]))
	VarDecl(y, ArrayType([3], IntegerType), ArrayLit([BinExpr(*, IntegerLit(2), IntegerLit(1)), BinExpr(*, IntegerLit(3), IntegerLit(2)), BinExpr(*, IntegerLit(4), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))   
       
    def test_more_complex_program_8(self):
        """More complex program"""
        input = """main: function void () {
            arr: array[2,3,4] of integer = {123,1231,23};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([2, 3, 4], IntegerType), ArrayLit([IntegerLit(123), IntegerLit(1231), IntegerLit(23)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308)) 
        
    def test_more_complex_program_9(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309)) 
        
    def test_more_complex_program_10(self):
        """More complex program"""
        input = """main: function array [2,3] of integer (n: integer) {
            x: integer = 65;
            y: array [2] of integer = {2, 4};
            printInt(1244123);
            writeFloat(1.23);
        }
        """
        expect = """Program([
	FuncDecl(main, ArrayType([2, 3], IntegerType), [Param(n, IntegerType)], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(65)), VarDecl(y, ArrayType([2], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(4)])), CallStmt(printInt, IntegerLit(1244123)), CallStmt(writeFloat, FloatLit(1.23))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310)) 
        
    def test_more_complex_program_11(self):
        """More complex program"""
        input = """
        main: function void () {
            for (x[1] = 2, x == 1, x + 1) {
            }
            y[1] = 2;
            z=100;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(x, [IntegerLit(1)]), IntegerLit(2)), BinExpr(==, Id(x), IntegerLit(1)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([])), AssignStmt(ArrayCell(y, [IntegerLit(1)]), IntegerLit(2)), AssignStmt(Id(z), IntegerLit(100))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_more_complex_program_12(self):
        """More complex program"""
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

        expect = """Program([
	FuncDecl(foo, FloatType, [Param(a, IntegerType), Param(b, FloatType)], bar, BlockStmt([AssignStmt(Id(a), IntegerLit(5)), AssignStmt(Id(b), BinExpr(*, IntegerLit(3), IntegerLit(5))), IfStmt(BinExpr(>, IntegerLit(3), IntegerLit(5)), AssignStmt(Id(c), FloatLit(123.123))), IfStmt(BinExpr(&&, BooleanLit(True), BooleanLit(False)), BlockStmt([AssignStmt(Id(d), BinExpr(+, Id(a), Id(b)))]), BlockStmt([AssignStmt(Id(d), Id(a))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))])), WhileStmt(BinExpr(>=, Id(a), Id(b)), AssignStmt(Id(a), BinExpr(-, Id(a), Id(b)))), DoWhileStmt(BinExpr(<, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), BreakStmt(), ContinueStmt(), ReturnStmt(BinExpr(+, Id(a), Id(b))), CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(go, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_more_complex_program_13(self):
        """More complex program"""
        input = """
        main: function void() {
        a:integer;
        a = -5*10/2 + 10;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(+, BinExpr(/, BinExpr(*, UnExpr(-, IntegerLit(5)), IntegerLit(10)), IntegerLit(2)), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_more_complex_program_14(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test_more_complex_program_15(self):
        """More complex program"""
        input = """main: function void () {
            delta: integer = fact(3);
            inc(x,delta);
            printint(x);
            return abc*func(2,3);
        } 
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printint, Id(x)), ReturnStmt(BinExpr(*, Id(abc), FuncCall(func, [IntegerLit(2), IntegerLit(3)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test_more_complex_program_16(self):
        """More complex program"""
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_more_complex_program_17(self):
        """More complex program"""
        input = """
        main: function void () {
            for (x[1] = 1, x == 1, x + 1) {
                t[2] = 3;
                y = x[10];
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(x, [IntegerLit(1)]), IntegerLit(1)), BinExpr(==, Id(x), IntegerLit(1)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(t, [IntegerLit(2)]), IntegerLit(3)), AssignStmt(Id(y), ArrayCell(x, [IntegerLit(10)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test_more_complex_program_18(self):
        """More complex program"""
        input = """
        main: function void () {
            for (x[1] = 6, x == 1, x + 1) {
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(x, [IntegerLit(1)]), IntegerLit(6)), BinExpr(==, Id(x), IntegerLit(1)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    
    def test_more_complex_program_19(self):
        """More complex program"""
        input = """
        main: function void(){
        
            x = a + b + c + 12;
            return \" hello,hi\";
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)), IntegerLit(12))), ReturnStmt(StringLit( hello,hi))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
       
    def test_more_complex_program_20(self):
        """More complex program"""
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
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
	FuncDecl(add, VoidType, [Param(i, FloatType)], None, BlockStmt([ReturnStmt(Id(i))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), InheritParam(delta, IntegerType), InheritOutParam(hallo, AutoType)], add, BlockStmt([AssignStmt(Id(n), BinExpr(+, BinExpr(+, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(-, BinExpr(-, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(*, BinExpr(*, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(/, BinExpr(/, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BooleanLit(True)), AssignStmt(Id(n), BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(%, Id(n), IntegerLit(1)), Id(hallo)), IntegerLit(1)), IntegerLit(2))), AssignStmt(Id(n), BinExpr(&&, BinExpr(&&, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(||, BinExpr(||, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(::, Id(n), Id(n))), AssignStmt(Id(n), BinExpr(+, Id(n), FuncCall(add, [Id(delta)]))), AssignStmt(Id(n), ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])])])), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
         
    def test_more_complex_program_21(self):
        """More complex program"""
        input = """main: function void() {
                x: array [2,3] of float = {{1.2, -2, 3.5e2}, {-2_3.5e10, -100.1, 2.3434}};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, IntegerLit(2)), FloatLit(350.0)]), ArrayLit([UnExpr(-, FloatLit(235000000000.0)), UnExpr(-, FloatLit(100.1)), FloatLit(2.3434)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_more_complex_program_22(self):
        """More complex program"""
        input = """main: function void() {
                x: array [2,3] of boolean = {{true, false, true}, {false, true, false}};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True)]), ArrayLit([BooleanLit(False), BooleanLit(True), BooleanLit(False)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test_more_complex_program_23(self):
        """More complex program"""
        input = """main: function array [2,3] of integer (n: integer) {
            x: integer = 65;
            y: array [2] of integer = {2, 4};
            printInt(1244123);
            writeFloat(.e23);
        }
        """
        expect = """Program([
	FuncDecl(main, ArrayType([2, 3], IntegerType), [Param(n, IntegerType)], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(65)), VarDecl(y, ArrayType([2], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(4)])), CallStmt(printInt, IntegerLit(1244123)), CallStmt(writeFloat, FloatLit(0.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test_more_complex_program_24(self):
        """More complex program"""
        input = """main: function void() {
            for (a = 1, a == 1, a + 1) {
                x = 1_234.5E-67;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(==, Id(a), IntegerLit(1)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), FloatLit(1.2345e-64))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test_more_complex_program_25(self):
        """More complex program"""
        input = """main: function void() {
        x:integer = foo(foo(1234));
        for (x=1,1,x+2) break;
        }"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(foo, [FuncCall(foo, [IntegerLit(1234)])])), ForStmt(AssignStmt(Id(x), IntegerLit(1)), IntegerLit(1), BinExpr(+, Id(x), IntegerLit(2)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test_more_complex_program_26(self):
        """More complex program"""
        input = """main: function void() {
        while (a[1] == 1) if (a == b) readInteger();
        }"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(readInteger, )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test_more_complex_program_27(self):
        """More complex program"""
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
        expect ="""Program([
	FuncDecl(foo, FloatType, [Param(a, IntegerType), Param(b, FloatType)], bar, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(t, IntegerType), VarDecl(u, IntegerType), VarDecl(v, IntegerType), AssignStmt(Id(x), IntegerLit(10)), AssignStmt(Id(y), IntegerLit(20)), AssignStmt(Id(z), BinExpr(+, Id(x), Id(y))), AssignStmt(Id(t), BinExpr(*, Id(z), IntegerLit(2))), AssignStmt(Id(u), BinExpr(/, Id(t), IntegerLit(4))), AssignStmt(Id(v), BinExpr(-, Id(u), IntegerLit(5))), CallStmt(writeInt, Id(v)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test_more_complex_program_28(self):
        """More complex program"""
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
        expect ="""Program([
	FuncDecl(fibo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(2))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(max)), CallStmt(fibo, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test_more_complex_program_29(self):
        """More complex program"""
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
        expect ="""Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(5)), AssignStmt(Id(b), BinExpr(*, IntegerLit(3), IntegerLit(5))), IfStmt(BinExpr(>, IntegerLit(3), IntegerLit(5)), AssignStmt(Id(c), FloatLit(123.123))), IfStmt(BinExpr(&&, BooleanLit(True), BooleanLit(False)), BlockStmt([AssignStmt(Id(d), BinExpr(+, Id(a), Id(b)))]), BlockStmt([AssignStmt(Id(d), Id(a))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))])), WhileStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), Id(b)))])), DoWhileStmt(BinExpr(<, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), BreakStmt(), ContinueStmt(), ReturnStmt(BinExpr(+, Id(a), Id(b))), CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(go, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test_more_complex_program_30(self):
        """More complex program"""
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
        expect ="""Program([
	VarDecl(a, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BooleanLit(True), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), BreakStmt()])), DoWhileStmt(BooleanLit(True), BlockStmt([ContinueStmt(), AssignStmt(Id(a), StringLit(1234)), AssignStmt(Id(a), BinExpr(::, Id(a), Id(a)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
            
    def test_more_complex_program_31(self):
                """Simple program"""
                input = """main: function void () {
                if(a || b) {
                a : integer = 3;
                return "abc";
            }
            else
                return "abc";
        }"""
                expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, Id(a), Id(b)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(3)), ReturnStmt(StringLit(abc))]), ReturnStmt(StringLit(abc)))]))
])"""
                self.assertTrue(TestAST.test(input, expect, 331))
        
    def test_more_complex_program_32(self):
        """Simple program"""
        input = """main: function void () {
            if(a == b + 4) {
                for( i = 0, i<10*a, i + b) {
                    if(i == 5)
                        break;
                    else {
                        foo("Tran Ngoc Bao Duy", "PPL");
                    }
                }
            }
            else {
                while(i < 100*a*b) {
                    printString("Gangzz");
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(+, Id(b), IntegerLit(4))), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(*, IntegerLit(10), Id(a))), BinExpr(+, Id(i), Id(b)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BreakStmt(), BlockStmt([CallStmt(foo, StringLit(Tran Ngoc Bao Duy), StringLit(PPL))]))]))]), BlockStmt([WhileStmt(BinExpr(<, Id(i), BinExpr(*, BinExpr(*, IntegerLit(100), Id(a)), Id(b))), BlockStmt([CallStmt(printString, StringLit(Gangzz))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))   
        
    def test_more_complex_program_33(self):
        """Simple program"""
        input = """main: function void () {
            for(i = 1*2, i >= 100, i * 4) {
                while(i % 4 == 0) {
                    printString("Ayyo whatsup!");
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(*, IntegerLit(1), IntegerLit(2))), BinExpr(>=, Id(i), IntegerLit(100)), BinExpr(*, Id(i), IntegerLit(4)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(4)), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(Ayyo whatsup!))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test_more_complex_program_34(self):
        """Simple program"""
        input = """main: function void () {
            do {
                if(i == 5)
                    break;
                i = i + 1;
            }
            while(i && 1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(&&, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BreakStmt()), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))    
     
    def test_more_complex_program_35(self):
        """Simple program"""
        input = """main: function void () {
            do {
                i = i + 1;
            }
            while(i && 1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(&&, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))   
        
    def test_more_complex_program_36(self):
        """Simple program"""
        input = """main: function void () {
            while(i < 10) {
                if(i == 5) {
                    a = 3;
                    break;
                }
                else {
                    i = i+1;
                    continue;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(Id(a), IntegerLit(3)), BreakStmt()]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_more_complex_program_37(self):
        """More complex program"""
        input = """main: function void () {
            a,b : array [3] of integer = {1,2,3}, {2,3,4};
            return a*main(1,2,3);
            }
            inc : function array [1] of integer (out n : integer , delta : integer ) inherit abc{
                n = n + delta ;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(b, ArrayType([3], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)])), ReturnStmt(BinExpr(*, Id(a), FuncCall(main, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))]))
	FuncDecl(inc, ArrayType([1], IntegerType), [OutParam(n, IntegerType), Param(delta, IntegerType)], abc, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test_more_complex_program_38(self):
        """More complex program"""
        input = """
        main: function void () {
            /* this is a block comment */
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_more_complex_program_39(self):
        """More complex program"""
        input = """main: function void() {
        a,b : integer = foo({123},{134}), foo({123},{134});
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(foo, [ArrayLit([IntegerLit(123)]), ArrayLit([IntegerLit(134)])])), VarDecl(b, IntegerType, FuncCall(foo, [ArrayLit([IntegerLit(123)]), ArrayLit([IntegerLit(134)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test_more_complex_program_40(self):
        """More complex program"""
        input = """main: function void() {
        x:integer = foo(foo(1234));
        for (x=1,1,x+2) break;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(foo, [FuncCall(foo, [IntegerLit(1234)])])), ForStmt(AssignStmt(Id(x), IntegerLit(1)), IntegerLit(1), BinExpr(+, Id(x), IntegerLit(2)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test_more_complex_program_41(self):
        """More complex program"""
        input = """
        delta: integer = fact({{"1234"}});
        a: integer = 5;
        """
        expect = """Program([
	VarDecl(delta, IntegerType, FuncCall(fact, [ArrayLit([ArrayLit([StringLit(1234)])])]))
	VarDecl(a, IntegerType, IntegerLit(5))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test_more_complex_program_42(self):
        """More complex program"""
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
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, BinExpr(%, Id(max), Id(n1)), IntegerLit(0)), BinExpr(==, BinExpr(%, Id(max), Id(n2)), IntegerLit(0))), BlockStmt([CallStmt(print, StringLit(LCM = )), CallStmt(printInteger, Id(max)), BreakStmt()]), AssignStmt(Id(max), BinExpr(+, Id(max), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_more_complex_program_43(self):
        """More complex program"""
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
        
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(z, BooleanType, BinExpr(==, Id(x), Id(y)))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(x), BlockStmt([CallStmt(print, StringLit(x is true))]), BlockStmt([CallStmt(print, StringLit(x is false))])), IfStmt(Id(y), BlockStmt([CallStmt(print, StringLit(y is true))]), BlockStmt([CallStmt(print, StringLit(y is false))])), IfStmt(Id(z), BlockStmt([CallStmt(print, StringLit(z is true))]), BlockStmt([CallStmt(print, StringLit(z is false))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_more_complex_program_44(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
    # ================================================================
    def test_more_complex_program_45(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test_more_complex_program_46(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test_more_complex_program_47(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_more_complex_program_48(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test_more_complex_program_49(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test_more_complex_program_50(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test_more_complex_program_51(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test_more_complex_program_52(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test_more_complex_program_53(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test_more_complex_program_54(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_more_complex_program_55(self):
        """More complex program"""
        input = """
        main: function void(){
            a: array[3,4] of integer = {1,2,3,4,5};
            return a[3];
        }
        """
        
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ReturnStmt(ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))    
         
    def test_more_complex_program_56(self):
        input = """ foo: function integer(x: integer){ }
                    bar: function float(y: float){ }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([]))
	FuncDecl(bar, FloatType, [Param(y, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_more_complex_program_57(self):
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
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	VarDecl(z, IntegerType, IntegerLit(30))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(bar, ), CallStmt(baz, )]))
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(y), Id(z)))]))
	FuncDecl(bar, VoidType, [], None, BlockStmt([AssignStmt(Id(y), BinExpr(+, Id(x), Id(z)))]))
	FuncDecl(baz, VoidType, [], None, BlockStmt([AssignStmt(Id(z), BinExpr(+, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_more_complex_program_58(self):
        input = """x: integer = 10; // This is x
        y: integer = 20; // This is y
        z: integer = 30; // This is z
        main: function void() {
            // This is a comment
            foo(); // Call foo
            bar(); // Call bar
            baz(); // Call baz
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
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	VarDecl(z, IntegerType, IntegerLit(30))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(bar, ), CallStmt(baz, )]))
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(y), Id(z)))]))
	FuncDecl(bar, VoidType, [], None, BlockStmt([AssignStmt(Id(y), BinExpr(+, Id(x), Id(z)))]))
	FuncDecl(baz, VoidType, [], None, BlockStmt([AssignStmt(Id(z), BinExpr(+, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_more_complex_program_59(self):
        input = """/* This is a block comment
        This is a multiline comment */ 
        x: integer = 10; 
        y: integer = 20; 
        z: integer = 30; 
        /* This is another comment */
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
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	VarDecl(z, IntegerType, IntegerLit(30))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(bar, ), CallStmt(baz, )]))
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(y), Id(z)))]))
	FuncDecl(bar, VoidType, [], None, BlockStmt([AssignStmt(Id(y), BinExpr(+, Id(x), Id(z)))]))
	FuncDecl(baz, VoidType, [], None, BlockStmt([AssignStmt(Id(z), BinExpr(+, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_more_complex_program_60(self):
        input = """/* This is a block comment
        This is a multiline comment */ 
        x: integer = 10; 
        y: integer = 20; 
        z: integer = 30; 
        /* This is another comment */
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
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	VarDecl(z, IntegerType, IntegerLit(30))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(bar, ), CallStmt(baz, )]))
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(y), Id(z)))]))
	FuncDecl(bar, VoidType, [], None, BlockStmt([AssignStmt(Id(y), BinExpr(+, Id(x), Id(z)))]))
	FuncDecl(baz, VoidType, [], None, BlockStmt([AssignStmt(Id(z), BinExpr(+, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_more_complex_program_61(self):
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
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(z, BooleanType, BinExpr(==, Id(x), Id(y)))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(x), BlockStmt([CallStmt(print, StringLit(x is true))]), BlockStmt([CallStmt(print, StringLit(x is false))])), IfStmt(Id(y), BlockStmt([CallStmt(print, StringLit(y is true))]), BlockStmt([CallStmt(print, StringLit(y is false))])), IfStmt(Id(z), BlockStmt([CallStmt(print, StringLit(z is true))]), BlockStmt([CallStmt(print, StringLit(z is false))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_more_complex_program_62(self):
        input = """x: string = "Hello";
        y: string = "World";
        z: string = x + y;
        main: function void() {
            print(z);
        }"""
        expect = """Program([
	VarDecl(x, StringType, StringLit(Hello))
	VarDecl(y, StringType, StringLit(World))
	VarDecl(z, StringType, BinExpr(+, Id(x), Id(y)))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_more_complex_program_63(self):
        input = """max:function integer(a: integer, b:integer, c:integer) {
            if (a > b) {
                if (a > c) {
                    return a;
                } else {
                    return c;
                }
            } else {
                if (b > c) {
                    return b;
                } else {
                    return c;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(max, IntegerType, [Param(a, IntegerType), Param(b, IntegerType), Param(c, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([IfStmt(BinExpr(>, Id(a), Id(c)), BlockStmt([ReturnStmt(Id(a))]), BlockStmt([ReturnStmt(Id(c))]))]), BlockStmt([IfStmt(BinExpr(>, Id(b), Id(c)), BlockStmt([ReturnStmt(Id(b))]), BlockStmt([ReturnStmt(Id(c))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_more_complex_program_64(self):
        input = """printMultiples: function void (n: integer) {
        for (i = 1, i <= 10, i + 1) {
        if (i * n > 100) {
            break;
        }
         print(i * n);
            }
        }"""
        expect = """Program([
	FuncDecl(printMultiples, VoidType, [Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, BinExpr(*, Id(i), Id(n)), IntegerLit(100)), BlockStmt([BreakStmt()])), CallStmt(print, BinExpr(*, Id(i), Id(n)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_more_complex_program_65(self):
        input = """sumArray:function integer(arr: array[3] of integer, n: integer) {
        sum = 0;
            for (i = 0, i < n,i + 1) {
        sum = sum + arr[i];
            }
            return sum;
        }"""
        expect = """Program([
	FuncDecl(sumArray, IntegerType, [Param(arr, ArrayType([3], IntegerType)), Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_more_complex_program_66(self):
        input = """isEven:function boolean(n: integer) {
            return (n % 2 == 0) && (n > 0);
        }"""
        expect = """Program([
	FuncDecl(isEven, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(==, BinExpr(%, Id(n), IntegerLit(2)), IntegerLit(0)), BinExpr(>, Id(n), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_more_complex_program_67(self):
        input = """swap: function void(a: integer,  b:integer) {
            temp = a;
            a = b;
            b = temp;
        }"""
        expect = """Program([
	FuncDecl(swap, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([AssignStmt(Id(temp), Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_more_complex_program_68(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        foo: function integer (a: integer, b: integer, c: integer) {
            return a + b * c;
        }
        bar: function integer (n: integer) {
            return foo(x, y, z) + n;
        }
        main: function void() {
            printIntLn(bar(5));
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	VarDecl(z, IntegerType, IntegerLit(30))
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType), Param(c, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), BinExpr(*, Id(b), Id(c))))]))
	FuncDecl(bar, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(foo, [Id(x), Id(y), Id(z)]), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntLn, FuncCall(bar, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_more_complex_program_69(self):
        input = """x: integer = 5;
        y: integer = 10;
        foo: function integer (a: integer, b: integer) {
            return a + b * (a - b);
        }
        bar: function boolean (n: integer) {
            return (n > 0) && (n < 10);
        }
        main: function void() {
            z: integer = foo(x + y, y - x) * 2 - 5;
            printIntLn(z);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(5))
	VarDecl(y, IntegerType, IntegerLit(10))
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), BinExpr(*, Id(b), BinExpr(-, Id(a), Id(b)))))]))
	FuncDecl(bar, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(0)), BinExpr(<, Id(n), IntegerLit(10))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(z, IntegerType, BinExpr(-, BinExpr(*, FuncCall(foo, [BinExpr(+, Id(x), Id(y)), BinExpr(-, Id(y), Id(x))]), IntegerLit(2)), IntegerLit(5))), CallStmt(printIntLn, Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_more_complex_program_70(self):
        input = """x: integer = 10;
        y: integer = 20;
        z: integer = 30;
        foo: function integer (a: integer, b: integer) {
            if (a > b) return a;
            else return b;
        }
        bar: function boolean (n: integer) {
            return (n >= x) && (n <= z);
        }
        main: function void() {
            if (bar(y)) print("y is in range");
            else print("y is out of range");
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	VarDecl(z, IntegerType, IntegerLit(30))
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(Id(b)))]))
	FuncDecl(bar, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(>=, Id(n), Id(x)), BinExpr(<=, Id(n), Id(z))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(bar, [Id(y)]), CallStmt(print, StringLit(y is in range)), CallStmt(print, StringLit(y is out of range)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

# """ """ """ """ """ """ """  """ """ """ """ """ """ """
    def test_more_complex_program_71(self):
        input = """
            foo: function float (a: integer, b: float) inherit bar { 
                a = 5;
                b = 3 * 5;
                if (3 > 5) c = 123.123;
                if( true && false) {d = a + b;} else {d = a;}
                for(i = 1, i < 10, i + 1) {writeInt(i);}
                while(a>= b) a = a - b;
                do {a = a + 1;} while (a < 100);
                return a + b;
            }
        """
        expect = """Program([
	FuncDecl(foo, FloatType, [Param(a, IntegerType), Param(b, FloatType)], bar, BlockStmt([AssignStmt(Id(a), IntegerLit(5)), AssignStmt(Id(b), BinExpr(*, IntegerLit(3), IntegerLit(5))), IfStmt(BinExpr(>, IntegerLit(3), IntegerLit(5)), AssignStmt(Id(c), FloatLit(123.123))), IfStmt(BinExpr(&&, BooleanLit(True), BooleanLit(False)), BlockStmt([AssignStmt(Id(d), BinExpr(+, Id(a), Id(b)))]), BlockStmt([AssignStmt(Id(d), Id(a))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))])), WhileStmt(BinExpr(>=, Id(a), Id(b)), AssignStmt(Id(a), BinExpr(-, Id(a), Id(b)))), DoWhileStmt(BinExpr(<, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test_more_complex_program_72(self):
        input = """
        x, y: integer;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_more_complex_program_73(self):
        input = """
            foo: function integer(a: integer, b: float) { 
                if (a > b) return a;
                else return int(b);
            }
            bar: function integer(a: integer, b: float) inherit foo { 
                return foo(a, b) + 1;
            }
            main: function void() {
                x: integer;
                y: float;
                x = 10;
                y = 20.5;
                writeInt(bar(x, y));
            }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(FuncCall(int, [Id(b)])))]))
	FuncDecl(bar, IntegerType, [Param(a, IntegerType), Param(b, FloatType)], foo, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(foo, [Id(a), Id(b)]), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType), AssignStmt(Id(x), IntegerLit(10)), AssignStmt(Id(y), FloatLit(20.5)), CallStmt(writeInt, FuncCall(bar, [Id(x), Id(y)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_more_complex_program_74(self):
        input = """
            a: integer;
            b: float;
            c: boolean;
            d: string;
            main: function integer () {
                a = 1;
                b = 2.0;
                c = true;
                d = "hello world";
                writeIntLn(a);
                writeFloatLn(b);
                writeBoolLn(c);
                writeStringLn(d);
            }
        """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, FloatType)
	VarDecl(c, BooleanType)
	VarDecl(d, StringType)
	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), FloatLit(2.0)), AssignStmt(Id(c), BooleanLit(True)), AssignStmt(Id(d), StringLit(hello world)), CallStmt(writeIntLn, Id(a)), CallStmt(writeFloatLn, Id(b)), CallStmt(writeBoolLn, Id(c)), CallStmt(writeStringLn, Id(d))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    
    def test_more_complex_program_75(self):
        input = """
            main: function void () inherit A {
                x: integer;
                y: float;
                z: integer;
                i: integer;
                x = 5;
                y = 2.5;
                z = x + y;
                for (i = 1, i < 10, i + 1) {
                    writeIntLn(i);
                }
                if (z > 10) {
                    writeStringLn("z is greater than 10");
                } else {
                    writeStringLn("z is less than or equal to 10");
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], A, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType), VarDecl(z, IntegerType), VarDecl(i, IntegerType), AssignStmt(Id(x), IntegerLit(5)), AssignStmt(Id(y), FloatLit(2.5)), AssignStmt(Id(z), BinExpr(+, Id(x), Id(y))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeIntLn, Id(i))])), IfStmt(BinExpr(>, Id(z), IntegerLit(10)), BlockStmt([CallStmt(writeStringLn, StringLit(z is greater than 10))]), BlockStmt([CallStmt(writeStringLn, StringLit(z is less than or equal to 10))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_more_complex_program_76(self):
        input = """
            foo: function integer(a: integer, b: integer) { 
                if (a == b) return a;
                else return foo(a + 1, b);
            }
            main: function void() {
                x: integer;
                x = foo(1, 5);
                writeIntLn(x);
            }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(FuncCall(foo, [BinExpr(+, Id(a), IntegerLit(1)), Id(b)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), FuncCall(foo, [IntegerLit(1), IntegerLit(5)])), CallStmt(writeIntLn, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_more_complex_program_77(self):
        input = """
            foo: function integer (x: integer) {
                if (x > 0) {
                    return x * foo(x - 1);
                }
                return 1;
            }
            main: function string () {
                writeInt(foo(5));
            }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(BinExpr(*, Id(x), FuncCall(foo, [BinExpr(-, Id(x), IntegerLit(1))])))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, StringType, [], None, BlockStmt([CallStmt(writeInt, FuncCall(foo, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_more_complex_program_78(self):
        input = """
        x: float = 12.e2;
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
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(1200.0))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test_more_complex_program_79(self):
        input = """
        voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                printInt(delta);
            }
        """
        expect = """Program([
	FuncDecl(voidA, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(n), IntegerLit(4)), IntegerLit(2)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(voidA, [FuncCall(voidA, [IntegerLit(34)])])), CallStmt(printInt, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))   
        
    def test_more_complex_program_80(self):
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(+, Id(x), IntegerLit(1))), ReturnStmt(Id(z))]))
	FuncDecl(bar, FloatType, [Param(y, FloatType)], None, BlockStmt([VarDecl(z, FloatType), AssignStmt(Id(z), BinExpr(*, Id(y), FloatLit(2.0))), ReturnStmt(Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))      
        
    def test_more_complex_program_81(self):
        input = """
            foo: function integer(a: integer, b: float) { 
                if (a > b) return a;
                else return cc(b);
            }
            main: function void () {
                x: integer;
                y: float;
                x = 10;
                y = 20.5;
                writeInt(foo(x, y));
            }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(FuncCall(cc, [Id(b)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType), AssignStmt(Id(x), IntegerLit(10)), AssignStmt(Id(y), FloatLit(20.5)), CallStmt(writeInt, FuncCall(foo, [Id(x), Id(y)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))   
        
    def test_more_complex_program_82(self):
        input = """foo: function boolean (a: boolean, b: boolean) {
            return (a || b) && (! a || b);
        }
        bar: function boolean (n: integer) {
            return (n > 0) && (n < 10);
        }
        main: function void() {
            printBoolLn(foo(true, false) || bar(5));
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(a, BooleanType), Param(b, BooleanType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(||, Id(a), Id(b)), BinExpr(||, UnExpr(!, Id(a)), Id(b))))]))
	FuncDecl(bar, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(0)), BinExpr(<, Id(n), IntegerLit(10))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolLn, BinExpr(||, FuncCall(foo, [BooleanLit(True), BooleanLit(False)]), FuncCall(bar, [IntegerLit(5)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_more_complex_program_83(self):
        input = """printOddNumbers:function void(n: integer) {
            i = 1;
            while (i <= n) {
                if (i % 2 == 0) {
                    i = i + 1;
                    continue;
                }
                print(i);
                i = i + 1;
            }
        }"""
        expect = """Program([
	FuncDecl(printOddNumbers, VoidType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(i), IntegerLit(1)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), ContinueStmt()])), CallStmt(print, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test_more_complex_program_84(self):
        input = """x: integer = 10;
        y: integer = 20;
        main: function void() {
            if (x > y) {
                print("x is greater than y");
            } else {
                print("x is less than or equal to y");
            }
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), Id(y)), BlockStmt([CallStmt(print, StringLit(x is greater than y))]), BlockStmt([CallStmt(print, StringLit(x is less than or equal to y))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test_more_complex_program_85(self):
        input = """main: function void() {
                x: array [2,3] of float = {{1.2, -2, .5e2}, {-2_3.5e10, -100.1, 2.3434}};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, IntegerLit(2)), FloatLit(50.0)]), ArrayLit([UnExpr(-, FloatLit(235000000000.0)), UnExpr(-, FloatLit(100.1)), FloatLit(2.3434)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test_more_complex_program_86(self):
        input = """main: function void() {
            while (a[1] == 1) a = a + 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test_more_complex_program_87(self):
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(+, Id(x), IntegerLit(1))), ReturnStmt(Id(z))]))
	FuncDecl(bar, FloatType, [Param(y, FloatType)], None, BlockStmt([VarDecl(z, FloatType), AssignStmt(Id(z), BinExpr(*, Id(y), FloatLit(2.0))), ReturnStmt(Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test_more_complex_program_88(self):
        input = """foo:function integer(x: integer, y: float) {
                z: integer;
                z = x + y;
                return z;
            }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType), Param(y, FloatType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(+, Id(x), Id(y))), ReturnStmt(Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test_more_complex_program_89(self):
        input = """swap: function void (arr: array[5] of integer, i: integer, j: integer) {
            temp: integer;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        """
        expect = """Program([
	FuncDecl(swap, VoidType, [Param(arr, ArrayType([5], IntegerType)), Param(i, IntegerType), Param(j, IntegerType)], None, BlockStmt([VarDecl(temp, IntegerType), AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), Id(temp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test_more_complex_program_90(self):
        input = """func: function void (a: integer, b: float, c: boolean) {
            x: integer;
            y: float = 3.14;
            z: boolean = true;
            if (c && b > 0) {
                x = a + y;
            }
            else {
                x = a - y;
            }
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType), Param(b, FloatType), Param(c, BooleanType)], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType, FloatLit(3.14)), VarDecl(z, BooleanType, BooleanLit(True)), IfStmt(BinExpr(>, BinExpr(&&, Id(c), Id(b)), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), Id(y)))]), BlockStmt([AssignStmt(Id(x), BinExpr(-, Id(a), Id(y)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    def test_more_complex_program_91(self):
        input = """x: integer = 10;
            y: integer = 20;
            z: integer = 30;
            foo: function integer (a: integer, b: integer) {
                if (a > b) return a;
                else return b;
            }
            bar: function boolean (n: integer) {
                return (n >= x) && (n <= z);
            }
            main: function void() {
                if (bar(y)) print("y is in range");
                else print("y is out of range");
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, IntegerType, IntegerLit(20))
	VarDecl(z, IntegerType, IntegerLit(30))
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(Id(b)))]))
	FuncDecl(bar, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(>=, Id(n), Id(x)), BinExpr(<=, Id(n), Id(z))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(bar, [Id(y)]), CallStmt(print, StringLit(y is in range)), CallStmt(print, StringLit(y is out of range)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test_more_complex_program_92(self):
        input = """x: integer = 5;
            y: integer = 10;
            foo: function integer (a: integer, b: integer) {
                return a + b * (a - b);
            }
            bar: function boolean (n: integer) {
                return (n > 0) && (n < 10);
            }
            main: function void() {
                z: integer = foo(x + y, y - x) * 2 - 5;
                printIntLn(z);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(5))
	VarDecl(y, IntegerType, IntegerLit(10))
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), BinExpr(*, Id(b), BinExpr(-, Id(a), Id(b)))))]))
	FuncDecl(bar, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(0)), BinExpr(<, Id(n), IntegerLit(10))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(z, IntegerType, BinExpr(-, BinExpr(*, FuncCall(foo, [BinExpr(+, Id(x), Id(y)), BinExpr(-, Id(y), Id(x))]), IntegerLit(2)), IntegerLit(5))), CallStmt(printIntLn, Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
        
    def test_more_complex_program_93(self):
        input = """foo: function boolean (a: boolean, b: boolean) {
                return (a || b) && (! a || b);
            }
            bar: function boolean (n: integer) {
                return (n > 0) && (n < 10);
            }
            main: function void() {
                printBoolLn(foo(true, false) || bar(5));
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(a, BooleanType), Param(b, BooleanType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(||, Id(a), Id(b)), BinExpr(||, UnExpr(!, Id(a)), Id(b))))]))
	FuncDecl(bar, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(0)), BinExpr(<, Id(n), IntegerLit(10))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolLn, BinExpr(||, FuncCall(foo, [BooleanLit(True), BooleanLit(False)]), FuncCall(bar, [IntegerLit(5)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test_more_complex_program_94(self):
        input = """sumArray:function integer(arr: array[3] of integer, n: integer) {
            sum = 0;
                for (i = 0, i < n,i + 1) {
            sum = sum + arr[i];
                }
                return sum;
        }"""
        expect = """Program([
	FuncDecl(sumArray, IntegerType, [Param(arr, ArrayType([3], IntegerType)), Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test_more_complex_program_95(self):
        input = """func: function void (a: integer, b: float, c: boolean) {
            x: integer;
            y: float = 3.14;
            z: boolean = true;
            if (c && b > 0) {
                x = a + y;
            }
            else {
                x = a - y;
            }
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType), Param(b, FloatType), Param(c, BooleanType)], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType, FloatLit(3.14)), VarDecl(z, BooleanType, BooleanLit(True)), IfStmt(BinExpr(>, BinExpr(&&, Id(c), Id(b)), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), Id(y)))]), BlockStmt([AssignStmt(Id(x), BinExpr(-, Id(a), Id(y)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test_more_complex_program_96(self):
        input = """printOddNumbers:function void(n: integer) {
            i = 1;
            while (i <= n) {
                if (i % 2 == 0) {
                    i = i + 1;
                    continue;
                }
                print(i);
                i = i + 1;
            }
        }"""
        expect = """Program([
	FuncDecl(printOddNumbers, VoidType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(i), IntegerLit(1)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), ContinueStmt()])), CallStmt(print, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test_more_complex_program_97(self):
        input = """func: function void (a: integer, b: float, c: boolean) {
            x: integer;
            y: float = 3.14;
            z: boolean = true;
            if (c && b > 0) {
                x = a + y;
            }
            else {
                x = a - y;
            }
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType), Param(b, FloatType), Param(c, BooleanType)], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, FloatType, FloatLit(3.14)), VarDecl(z, BooleanType, BooleanLit(True)), IfStmt(BinExpr(>, BinExpr(&&, Id(c), Id(b)), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), Id(y)))]), BlockStmt([AssignStmt(Id(x), BinExpr(-, Id(a), Id(y)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test_more_complex_program_97(self):
        input = """isEven:function boolean(n: integer) {
            return (n % 2 == 0) && (n > 0);
        }"""
        expect = """Program([
	FuncDecl(isEven, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(==, BinExpr(%, Id(n), IntegerLit(2)), IntegerLit(0)), BinExpr(>, Id(n), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test_more_complex_program_98(self):
        input = '''
            funcA: function integer(n: integer) inherit funcB{
                return n%10;
            }
            funcB: function void (out n: integer, n: integer){
                n = n + voidA(n);
            }
            main: function void () {
                n: integer = 10;
                funcB(x,n);
                return n;
            }
        '''
        expect = """Program([
	FuncDecl(funcA, IntegerType, [Param(n, IntegerType)], funcB, BlockStmt([ReturnStmt(BinExpr(%, Id(n), IntegerLit(10)))]))
	FuncDecl(funcB, VoidType, [OutParam(n, IntegerType), Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), FuncCall(voidA, [Id(n)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, IntegerLit(10)), CallStmt(funcB, Id(x), Id(n)), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test_more_complex_program_99(self):
        input = """a: array[5] of integer = {1, 2, 3, 4, 5};
                func: function integer(low: integer, high: integer) {
                    if ((low < 0) || (high < 0) || (low >= 5) || (high >= 5))
                        return -1;

                    sum = 0;
                    for (i = low, i <= high, i+1)
                        sum = sum + a[i];
                    return sum;
                }
            """
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(func, IntegerType, [Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(<, Id(low), IntegerLit(0)), BinExpr(<, Id(high), IntegerLit(0))), BinExpr(>=, Id(low), IntegerLit(5))), BinExpr(>=, Id(high), IntegerLit(5))), ReturnStmt(UnExpr(-, IntegerLit(1)))), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), Id(low)), BinExpr(<=, Id(i), Id(high)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(a, [Id(i)])))), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
        