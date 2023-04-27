def test_more_complex_program_20(self):
        """More complex program"""
        input = """
        main: function void(){
            for(x = y + z, x < z, x + y) {
                return x + y + z * 3;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)), IntegerLit(12))), ReturnStmt(StringLit( hello,hi))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))