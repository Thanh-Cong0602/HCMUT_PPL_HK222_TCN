import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # TEST INT_LIT
    def test_intlit_1(self):
        self.assertTrue(TestLexer.test("7", "7,<EOF>", 101))

    def test_intlit_2(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 102))

    def test_intlit_3(self):
        self.assertTrue(TestLexer.test("0123", "Error Token 0", 103))

    def test_intlit_4(self):
        self.assertTrue(TestLexer.test("12300", "12300,<EOF>", 104))

    def test_intlit_5(self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 105))

    def test_intlit_6(self):
        self.assertTrue(TestLexer.test("1__2__3", "1,__2__3,<EOF>", 106))

    def test_intlit_7(self):
        self.assertTrue(TestLexer.test("_123", "_123,<EOF>", 107))

    def test_intlit_8(self):
        self.assertTrue(TestLexer.test("123_", "123,_,<EOF>", 108))

    def test_intlit_9(self):
        self.assertTrue(TestLexer.test("_", "_,<EOF>", 109))

    def test_intlit_10(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 110))

    # TEST FLOAT_INT
    def test_float_lit1(self):
        self.assertTrue(TestLexer.test("0e123", "0e123,<EOF>", 111))

    def test_float_lit2(self):
        self.assertTrue(TestLexer.test("1.0", "1.0,<EOF>", 112))

    def test_float_lit3(self):
        self.assertTrue(TestLexer.test("0.1", "0.1,<EOF>", 113))

    def test_float_lit4(self):
        self.assertTrue(TestLexer.test("1_23.456", "123.456,<EOF>", 114))

    def test_float_lit5(self):
        self.assertTrue(TestLexer.test(".1", ".,1,<EOF>", 115))
        
    def test_float_lit6(self):
        """ Test Float Leading Zero """
        self.assertTrue(TestLexer.test(
            """
    00001.1101010101000
    0e-432
    000000001e-542400
    000313121.e00031321132
                """,

            "Error Token 0",
            116
        ))

    def test_float_lit7(self):
        self.assertTrue(TestLexer.test(
            ".", ".,<EOF>", 117))

    def test_float_lit8(self):
        self.assertTrue(TestLexer.test("00.1", "Error Token 0", 118))

    def test_float_lit9(self):
        self.assertTrue(TestLexer.test("0.0", "0.0,<EOF>", 119))

    # def test_float_11(self):
    #     self.assertTrue(TestLexer.test("1.23e4_56", "1.23e456,<EOF>", 111))

    def test_float_lit10(self):
        self.assertTrue(TestLexer.test("1.23e456", "1.23e456,<EOF>", 120))

    #TEST IDENTIFIER: 
    def test_identifiers_1(self):
        self.assertTrue(TestLexer.test("My Hanh", "My,Hanh,<EOF>", 121))

    def test_valid_identifier2(self):
        """Test Valid Identifiers"""
        input = """id boolean_id float_id int_id string_id void_id"""
        output = "id,boolean_id,float_id,int_id,string_id,void_id,<EOF>"
        self.assertTrue(TestLexer.test( input, output,122))

    def test_intlit_11(self):
        self.assertTrue(TestLexer.test("0000", "Error Token 0", 123))
    # TEST NUMBER LITERALS (FULL)
    def test39(self):
        self.assertTrue(TestLexer.test('==', '==,<EOF>', 124))

    def test40(self):
        self.assertTrue(TestLexer.test('!=', '!=,<EOF>', 125))

    def test41(self):
        self.assertTrue(TestLexer.test('<', '<,<EOF>', 126))

    def test42(self):
        self.assertTrue(TestLexer.test('<=', '<=,<EOF>', 127))

    def test_literals_1(self):
        self.assertTrue(TestLexer.test("0 1 2 3 4", "0,1,2,3,4,<EOF>", 128))

    def test_literals_2(self):
        self.assertTrue(TestLexer.test(
            "10 20 30 40", "10,20,30,40,<EOF>", 129))

    def test_literals_3(self):
        self.assertTrue(TestLexer.test("1.0 2.5 3.1415 100.123",
                        "1.0,2.5,3.1415,100.123,<EOF>", 130))

    def test_literals_4(self):
        self.assertTrue(TestLexer.test(
            "\"Hello, World!\"", "Hello, World!,<EOF>", 131))

    def test_literals_5(self):
        self.assertTrue(TestLexer.test("\"12345\"", "12345,<EOF>", 132))
        
    #TEST OPERATOR (OKE)

    def test_plus_operator(self):
        self.assertTrue(TestLexer.test("a + b", "a,+,b,<EOF>", 133))

    def test_minus_operator(self):
        self.assertTrue(TestLexer.test("a - b", "a,-,b,<EOF>", 134))

    def test_multiply_operator(self):
        self.assertTrue(TestLexer.test("a * b", "a,*,b,<EOF>", 135))

    def test_divide_operator(self):
        self.assertTrue(TestLexer.test("a / b", "a,/,b,<EOF>", 136))

    def test_modulo_operator(self):
        self.assertTrue(TestLexer.test("a % b", "a,%,b,<EOF>", 137))

    def test_assign_operator(self):
        self.assertTrue(TestLexer.test("a = b", "a,=,b,<EOF>", 138))

    def test_equal_operator(self):
        self.assertTrue(TestLexer.test("a == b", "a,==,b,<EOF>", 139))

    def test_not_equal_operator(self):
        self.assertTrue(TestLexer.test("a != b", "a,!=,b,<EOF>", 140))

    def test_less_than_operator(self):
        self.assertTrue(TestLexer.test("a < b", "a,<,b,<EOF>", 141))

    def test_less_than_or_equal_operator(self):
        self.assertTrue(TestLexer.test("a <= b", "a,<=,b,<EOF>", 142))

    def test_greater_than_operator(self):
        self.assertTrue(TestLexer.test("a > b", "a,>,b,<EOF>", 143))

    def test_greater_than_or_equal_operator(self):
        self.assertTrue(TestLexer.test("a >= b", "a,>=,b,<EOF>", 144))

    def test_logical_and_operator(self):
        self.assertTrue(TestLexer.test("a and b", "a,and,b,<EOF>", 145))

    def test_logical_or_operator(self):
        self.assertTrue(TestLexer.test("a or b", "a,or,b,<EOF>", 146))

    def test_logical_not_operator(self):
        self.assertTrue(TestLexer.test("not a", "not,a,<EOF>", 147))

    def test_left_parenthesis(self):
        self.assertTrue(TestLexer.test("( a + b )", "(,a,+,b,),<EOF>", 148))

    def test_right_parenthesis(self):
        self.assertTrue(TestLexer.test(
            "( a + b ) * c", "(,a,+,b,),*,c,<EOF>", 149))

    def test_comma_punctuation(self):
        self.assertTrue(TestLexer.test("a, b, c", "a,,,b,,,c,<EOF>", 150))

    def test_colon_punctuation(self):
        self.assertTrue(TestLexer.test("if a == b: pass",
                        "if,a,==,b,:,pass,<EOF>", 151))

    def test_semicolon_punctuation(self):
        self.assertTrue(TestLexer.test("a = b; print(a)",
                        "a,=,b,;,print,(,a,),<EOF>", 152))
        
        
        # TEST PUNCTUATIONS: <oke>

    def test_punctuation_1(self):
        self.assertTrue(TestLexer.test(",", ",,<EOF>", 153))

    def test_punctuation_2(self):
        self.assertTrue(TestLexer.test(";", ";,<EOF>", 154))

    def test_punctuation_3(self):
        self.assertTrue(TestLexer.test(":", ":,<EOF>", 155))

    def test_punctuation_4(self):
        self.assertTrue(TestLexer.test("(", "(,<EOF>", 156))

    def test_punctuation_5(self):
        self.assertTrue(TestLexer.test(")", "),<EOF>", 157))

    # TEST BRACKETS

    def test_brackets_1(self):
        self.assertTrue(TestLexer.test(
            "{ } [ ] ( )", "{,},[,],(,),<EOF>", 158))

    def test_brackets_2(self):
        self.assertTrue(TestLexer.test("({})[]", "(,{,},),[,],<EOF>", 159))

    def test_special_chars_1(self):
        self.assertTrue(TestLexer.test("{", "{,<EOF>", 160))

    def test_special_chars_2(self):
        self.assertTrue(TestLexer.test("}", "},<EOF>", 161))

    def test_string_68(self):
        input=r'''"""im not fvcking completed!""'''
        expect=r''',im not fvcking completed!,Unclosed String: '''
        self.assertTrue(TestLexer.test(input,expect,162))

    # TEST COMMENT
    # Test C-style comment
    def test_c_style_comment_1(self):
        self.assertTrue(TestLexer.test(
            "/* this is a comment */", "<EOF>", 163))

    def test_c_style_comment_2(self):
        self.assertTrue(TestLexer.test(
            "/* this is a\nmulti-line\ncomment */", "<EOF>", 164))

    def test_c_style_comment_3(self):
        self.assertTrue(TestLexer.test(
            "a=5/* this is a comment */b=6", "a,=,5,b,=,6,<EOF>", 165))

    def test_c_style_comment_4(self):
        self.assertTrue(TestLexer.test("/* this is not a comment",
                        "/,*,this,is,not,a,comment,<EOF>", 166))

    def test_cpp_style_comment_1(self):
        self.assertTrue(TestLexer.test("// this is a comment", "<EOF>", 167))

    def test_cpp_style_comment_2(self):
        self.assertTrue(TestLexer.test(
            "// this is a comment\na=5", "a,=,5,<EOF>", 168))

    def test_cpp_style_comment_3(self):
        self.assertTrue(TestLexer.test(
            "a=5// this is a comment\nb=6", "a,=,5,b,=,6,<EOF>", 169))

    def test_cpp_style_comment_4(self):
        self.assertTrue(TestLexer.test(
            "// this is not a comment", "<EOF>", 170))

    # Test C-style and C++-style comment
    def test_comment_1(self):
        self.assertTrue(TestLexer.test(
            "a=5; /* this is a comment */ b=6", "a,=,5,;,b,=,6,<EOF>", 171))

    def test_comment_2(self):
        self.assertTrue(TestLexer.test(
            "a=5; // this is a comment\nb=6", "a,=,5,;,b,=,6,<EOF>", 172))

    def test_comment_3(self):
        self.assertTrue(TestLexer.test(
            "/* this is a comment */ a=5; // this is a comment\nb=6", "a,=,5,;,b,=,6,<EOF>", 173))

    def test_comment_4(self):
        self.assertTrue(TestLexer.test(
            "a=5; /* this is a comment // nested comment */ b=6", "a,=,5,;,b,=,6,<EOF>", 174))

    def test_comment_5(self):
        self.assertTrue(TestLexer.test(
            "a=5; /* this is a\nmulti-line\ncomment */ b=6", "a,=,5,;,b,=,6,<EOF>", 175))

    def test_comment_6(self):
        self.assertTrue(TestLexer.test(
            "// this is a comment\n/* this is a comment */\na=5; b=6", "a,=,5,;,b,=,6,<EOF>", 176))

    def test_comment_7(self):
        self.assertTrue(TestLexer.test(
            "/* this is a comment */ a=5; // this is a comment\nb=6", "a,=,5,;,b,=,6,<EOF>", 177))

    def test_comment_8(self):
        self.assertTrue(TestLexer.test(
            "a=5;// this is a comment", "a,=,5,;,<EOF>", 178))

    def test_comment_9(self):
        self.assertTrue(TestLexer.test(
            "a=5/* this is a comment */", "a,=,5,<EOF>", 179))

    def test80(self):
        self.assertTrue(TestLexer.test('""', ',<EOF>', 180))

    def test81(self):
        self.assertTrue(TestLexer.test('" "', ' ,<EOF>', 181))

    def test82(self):
        self.assertTrue(TestLexer.test(
            '"Hello, World!"', 'Hello, World!,<EOF>', 182))

    def test83(self):
        self.assertTrue(TestLexer.test(
            '"HELLO, WORLD!"', 'HELLO, WORLD!,<EOF>', 183))

    def test84(self):
        self.assertTrue(TestLexer.test('"The quick brown fox jumps over the lazy dog"',
                        'The quick brown fox jumps over the lazy dog,<EOF>', 184))

    def test85(self):
        self.assertTrue(TestLexer.test('"1234"', '1234,<EOF>', 185))

    def test86(self):
        self.assertTrue(TestLexer.test('"dat123"', 'dat123,<EOF>', 186))

    def test87(self):
        self.assertTrue(TestLexer.test(
            '"h3llo W0rld!"', 'h3llo W0rld!,<EOF>', 187))

    def test88(self):
        """ Test Block Comment """
        input = """
        /* This is a block comment */
        // This is a line comment
        /* Comment with multiple lines
            Hello comments
        */
        /*
            Comment multiple lines
        */
        /* nest comments
            // inline comment 
        // inline comment
        */
                """
        output = "<EOF>"
        self.assertTrue(TestLexer.test(input, output,188))

    def test89(self):
        self.assertTrue(TestLexer.test(
            '"Hello World"', 'Hello World,<EOF>', 189))

    def test90(self):
        self.assertTrue(TestLexer.test('"Line 1\\nnLine 2"',
                        'Line 1\\nnLine 2,<EOF>', 190))

    def test91(self):
        self.assertTrue(TestLexer.test(
            '"Line 1\\tLine 2"', 'Line 1\\tLine 2,<EOF>', 191))

    def test_invalid_identifier2(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.test(
            """
        123abc 123_abc 00000123_123abc
        id_id 1id 321id 1321_id 89________________id
        id___2 90___abc__ads___sba____abc____dba ds&a
                    """,
                "123,abc,123,_abc,Error Token 0",
            192
        ))

    def test93(self):
        self.assertTrue(TestLexer.test(
            '"Line 1\\fLine 2"', 'Line 1\\fLine 2,<EOF>', 193))

    def test94(self):
        self.assertTrue(TestLexer.test(
            '"Line 1\\rLine 2"', 'Line 1\\rLine 2,<EOF>', 194))

    def test95(self):
        self.assertTrue(TestLexer.test('$user', 'Error Token $', 195))

    def test96(self):
        self.assertTrue(TestLexer.test(
            r"""
                Illegal"\a"
            """,
            r"""Illegal,Illegal Escape In String: \a""",
            196
        ))

    def test97(self):
        self.assertTrue(TestLexer.test('"He asked me: \\"Where is \\"John?\\""',
                        'He asked me: \\"Where is \\"John?\\",<EOF>', 197))

    def test_string_70(self):
        input='"Wrong escape: \\x";'
        expect=r'''Illegal Escape In String: Wrong escape: \x'''
        self.assertTrue(TestLexer.test(input,expect,198))

    def test99(self):
        self.assertTrue(TestLexer.test('a, b, c: integer = 3, 4,6;',
                        'a,,,b,,,c,:,integer,=,3,,,4,,,6,;,<EOF>', 199))

    def test_valid_identifier1(self):
        """Test Valid Identifiers"""
        input = """a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
    _ _abc _123 _abc123 _abc_123 _123_abc
    __ ____ ____123____
    abc ABC aBC Abc _ABC __ABc __123ABc
    hdad_adsajdk_hf__T_"""
        output = "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,hdad_adsajdk_hf__T_,<EOF>"
        self.assertTrue(TestLexer.test( input, output,200))