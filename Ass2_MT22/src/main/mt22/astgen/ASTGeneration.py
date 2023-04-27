from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from collections import deque
id_list = deque()
expr_list = deque()
  
class ASTGeneration(MT22Visitor):
    
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        declList = []
        for x in ctx.decl():
            decl = self.visitDecl(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)
    
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        id_list.clear()
        expr_list.clear()
        if ctx.getChildCount() == 2:
            return self.visitVar_decl(ctx.var_decl())
        else:
            return self.visitFunc_decl(ctx.func_decl())

    def visitVar_decl(self, ctx: MT22Parser.Var_declContext):
        if ctx.getChildCount() == 5 and ctx.var_decl():
            id_list.append(str(ctx.getChild(0).getText())) 
            expr_list.append(self.visitExpr(ctx.expr()))
            return self.visitVar_decl(ctx.var_decl())
        elif ctx.ASSIGN(): 
            list_type = self.visitList_type(ctx.list_type())
            id_list.append(str(ctx.IDENTIFIER(0).getText())) 
            expr_list.append(self.visitExpr(ctx.expr()))
            if len(expr_list) > 1: expr_list.reverse()
        else:
            list_type = self.visitList_type(ctx.list_type())
            for x in ctx.IDENTIFIER():
                id_list.append(str(ctx.IDENTIFIER(ctx.IDENTIFIER().index(x)).getText()))
        if len(expr_list) == 0:
            return [VarDecl(x,list_type) for x in id_list]
        else:
            return [VarDecl(i, list_type, j) for i,j in zip(id_list,expr_list)]
    
    def visitArr_type(self, ctx:MT22Parser.Arr_typeContext):
        atomic_types = self.visitAtomic_types(ctx.atomic_types())
        dimensions = [int(ctx.INT_LIT(ctx.INT_LIT().index(x)).getText()) for x in ctx.INT_LIT()]
        return ArrayType(dimensions,atomic_types)
        # int_list = []
        # for x in ctx.INT_LIT():
        # int_list.append(int(ctx.INT_LIT(ctx.INT_LIT().index(x)).getText()))
    
    def visitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):   
        if ctx.INT(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STR(): return StringType()
        if ctx.BOOLEAN(): return BooleanType() 
    
    def visitList_type(self, ctx:MT22Parser.List_typeContext):
        if ctx.INT(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STR(): return StringType()
        if ctx.BOOLEAN(): return BooleanType()
        if ctx.AUTO(): return AutoType()
        if ctx.VOID(): return VoidType()
        if ctx.arr_type(): return self.visitArr_type(ctx.arr_type())
        
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        list_type = self.visitList_type(ctx.list_type())
        para_list = self.visitPara_list(ctx.para_list())
        block_stmt = self.visitBlock_stmt(ctx.block_stmt())
        id = ctx.IDENTIFIER(0).getText()
        return FuncDecl(id, list_type, para_list, ctx.IDENTIFIER(1).getText() if ctx.INHERIT() else "",block_stmt)
    
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
        return [self.visitPara(x) for x in ctx.para()]
     
    def visitPara(self, ctx:MT22Parser.ParaContext):
        list_type = self.visitList_type(ctx.list_type()) 
        id = ctx.IDENTIFIER().getText()
        return ParamDecl(id, list_type, True if ctx.OUT() else False, True if ctx.INHERIT() else False)
    
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        memBlock = []
        for i in ctx.stmt_vardecl():
            stmt_vardecls = self.visitStmt_vardecl(i)
            if isinstance(stmt_vardecls, list):
                memBlock.extend(stmt_vardecls)
            else:
                memBlock.append(stmt_vardecls)
        return BlockStmt(memBlock)
    
    def visitStmt_vardecl(self, ctx:MT22Parser.Stmt_vardeclContext):
        if ctx.getChildCount() == 1:
            return self.visitStmt(ctx.stmt())
        else:
            id_list.clear()
            expr_list.clear()
            return self.visitVar_decl(ctx.var_decl())
    
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.expr():
            return self.visitExpr(ctx.expr())
        else:
            return self.visitChildren(ctx)
        
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        if ctx.IF() and ctx.ELSE():
            return IfStmt(self.visitExpr(ctx.expr()), self.visitStmt(ctx.stmt(0)), self.visitStmt(ctx.stmt(1)))
        else:
            return IfStmt(self.visitExpr(ctx.expr()), self.visitStmt(ctx.stmt(0)))
        
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        expr = [self.visitExpr(x) for x in ctx.expr()]
        stmt = self.visitStmt(ctx.stmt())
        return ForStmt(self.visit(ctx.getChild(2)), expr[0], expr[1], stmt)
    
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        if ctx.getChild(0) == ctx.IDENTIFIER():
            id = Id(ctx.getChild(0).getText())
        else: 
            id = self.visit(ctx.getChild(0))
        return AssignStmt(id, self.visit(ctx.getChild(2)))
    
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return WhileStmt(self.visitExpr_while(ctx.expr_while()), self.visitStmt(ctx.stmt()))
     
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return DoWhileStmt(self.visitExpr(ctx.expr_while()), self.visitBlock_stmt(ctx.block_stmt()))
    
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()
    
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()
    
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return ReturnStmt(self.visitExpr(ctx.expr())) if ctx.expr() else ReturnStmt() 
        
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        id = ctx.IDENTIFIER().getText()
        return CallStmt(id, self.visitExpr_list(ctx.expr_list()))
    
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        id = ctx.getChild(0).getText()
        expr_list = self.visitExpr_list(ctx.expr_list())
        return FuncCall(id, expr_list)
    
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return [self.visitExpr(i) for i in ctx.expr()]
        
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitRelation_expr(self, ctx:MT22Parser.Relation_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else: 
            return self.visit(ctx.getChild(0))
        
    def visitLogic_expr(self, ctx:MT22Parser.Logic_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))

    def visitAdd_expr(self, ctx:MT22Parser.Add_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))
      
    def visitMul_expr(self, ctx:MT22Parser.Mul_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitNot_expr(self, ctx:MT22Parser.Not_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            return UnExpr(op, body)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            return UnExpr(op, body)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitExp9(self, ctx:MT22Parser.Exp9Context):
            return self.visit(ctx.getChild(0))
    
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        if ctx.func_call():
            return self.visitFunc_call(ctx.func_call())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            text = ctx.FLOAT_LIT().getText()
            # if text[1] == 'e': text = '0.0' 
            # .e23 = 0.0
            text = '0' + text
            return FloatLit(float(text))
        elif ctx.STRING_LIT():
            return StringLit(str(ctx.STRING_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLit(True if ctx.BOOL_LIT().getText() == 'true' else False)
        elif ctx.array():
            return self.visit(ctx.array())
        else:
            return self.visitExpr(ctx.expr())
        
    def visitIndex_operators(self, ctx:MT22Parser.Index_operatorsContext):
        id = ctx.IDENTIFIER().getText()
        return ArrayCell(id, self.visitExpr_list(ctx.expr_list()))   
    
    def visitArray(self, ctx:MT22Parser.ArrayContext):
        value = self.visit(ctx.literal_element()) 
        return ArrayLit(value) 
    
    def visitLiteral_element(self, ctx:MT22Parser.Literal_elementContext):
        return [self.visitLiteral(i) for i in ctx.literal()]
    
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)
        
    
    #   BEGIN EXPRESSIONS WITHOUT ARRAY IN ASSIGN     
    def visitExpr_while(self, ctx:MT22Parser.Expr_whileContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitRelation_expr1(self, ctx:MT22Parser.Relation_expr1Context):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else: 
            return self.visit(ctx.getChild(0))
        
    def visitLogic_expr1(self, ctx:MT22Parser.Logic_expr1Context):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))

    def visitAdd_expr1(self, ctx:MT22Parser.Add_expr1Context):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))
      
    def visitMul_expr1(self, ctx:MT22Parser.Mul_expr1Context):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return BinExpr(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitNot_expr1(self, ctx:MT22Parser.Not_expr1Context):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            return UnExpr(op, body)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitSign_expr1(self, ctx:MT22Parser.Sign_expr1Context):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            return UnExpr(op, body)
        else:
            return self.visit(ctx.getChild(0))
        
    def visitExp91(self, ctx:MT22Parser.Exp91Context):
        if ctx.expr_while():
            return self.visitExpr_while(ctx.expr_while())
        else:
            return self.visitOperand1(ctx.operand1())
    
    def visitOperand1(self, ctx:MT22Parser.Operand1Context):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            text = ctx.FLOAT_LIT().getText()
            if text[1] == 'e': text = '0.0'
            return FloatLit(float(text))
        elif ctx.STRING_LIT():
            return StringLit(str(ctx.STRING_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLit(True if ctx.BOOL_LIT().getText() == 'true' else False)
        elif ctx.func_call():
            return self.visitFunc_call(ctx.func_call())
        else:
            return self.visitIndex_operators1(ctx.index_operators1())
        
    def visitIndex_operators1(self, ctx:MT22Parser.Index_operatorsContext):
        id = ctx.IDENTIFIER().getText()
        return ArrayCell(id, self.visitExpr_list1(ctx.expr_list1()))    
    
    def visitExpr_list1(self, ctx:MT22Parser.Expr_listContext):
        return [self.visitExpr_while(i) for i in ctx.expr_while()]