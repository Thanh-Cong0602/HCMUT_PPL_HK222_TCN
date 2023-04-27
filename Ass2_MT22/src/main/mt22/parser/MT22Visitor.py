# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr_type.
    def visitArr_type(self, ctx:MT22Parser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_types.
    def visitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_type.
    def visitList_type(self, ctx:MT22Parser.List_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para.
    def visitPara(self, ctx:MT22Parser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_list.
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_vardecl.
    def visitStmt_vardecl(self, ctx:MT22Parser.Stmt_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relation_expr.
    def visitRelation_expr(self, ctx:MT22Parser.Relation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logic_expr.
    def visitLogic_expr(self, ctx:MT22Parser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#add_expr.
    def visitAdd_expr(self, ctx:MT22Parser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_expr.
    def visitMul_expr(self, ctx:MT22Parser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#not_expr.
    def visitNot_expr(self, ctx:MT22Parser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp9.
    def visitExp9(self, ctx:MT22Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operators.
    def visitIndex_operators(self, ctx:MT22Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_while.
    def visitExpr_while(self, ctx:MT22Parser.Expr_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relation_expr1.
    def visitRelation_expr1(self, ctx:MT22Parser.Relation_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logic_expr1.
    def visitLogic_expr1(self, ctx:MT22Parser.Logic_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#add_expr1.
    def visitAdd_expr1(self, ctx:MT22Parser.Add_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_expr1.
    def visitMul_expr1(self, ctx:MT22Parser.Mul_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#not_expr1.
    def visitNot_expr1(self, ctx:MT22Parser.Not_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr1.
    def visitSign_expr1(self, ctx:MT22Parser.Sign_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp91.
    def visitExp91(self, ctx:MT22Parser.Exp91Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand1.
    def visitOperand1(self, ctx:MT22Parser.Operand1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list1.
    def visitExpr_list1(self, ctx:MT22Parser.Expr_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operators1.
    def visitIndex_operators1(self, ctx:MT22Parser.Index_operators1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array.
    def visitArray(self, ctx:MT22Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal_element.
    def visitLiteral_element(self, ctx:MT22Parser.Literal_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_arr.
    def visitId_arr(self, ctx:MT22Parser.Id_arrContext):
        return self.visitChildren(ctx)



del MT22Parser