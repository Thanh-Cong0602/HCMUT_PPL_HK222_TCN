# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01d8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\3\3\3\5\3\u008e\n\3\3\3\6\3\u0091\n")
        buf.write("\3\r\3\16\3\u0092\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\5\b\u00a0\n\b\3\t\3\t\7\t\u00a4\n\t\f\t\16\t")
        buf.write("\u00a7\13\t\3\n\3\n\7\n\u00ab\n\n\f\n\16\n\u00ae\13\n")
        buf.write("\3\n\5\n\u00b1\n\n\3\n\7\n\u00b4\n\n\f\n\16\n\u00b7\13")
        buf.write("\n\3\n\5\n\u00ba\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00c3\n\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ca\n")
        buf.write("\13\3\13\3\13\3\f\3\f\5\f\u00d0\n\f\3\r\3\r\7\r\u00d4")
        buf.write("\n\r\f\r\16\r\u00d7\13\r\3\r\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\7-\u016d\n-\f-\16-\u0170\13-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38")
        buf.write("\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3")
        buf.write(">\7>\u019d\n>\f>\16>\u01a0\13>\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\7?\u01ab\n?\f?\16?\u01ae\13?\3?\3?\3@\6@\u01b3\n")
        buf.write("@\r@\16@\u01b4\3@\3@\3A\3A\6A\u01bb\nA\rA\16A\u01bc\3")
        buf.write("A\3A\3B\3B\7B\u01c3\nB\fB\16B\u01c6\13B\3B\3B\3C\3C\7")
        buf.write("C\u01cc\nC\fC\16C\u01cf\13C\3C\3C\3C\3C\3C\3D\3D\3D\3")
        buf.write("\u019e\2E\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\3\25\4")
        buf.write("\27\5\31\6\33\7\35\b\37\t!\n#\13%\f\'\r)\16+\17-\20/\21")
        buf.write("\61\22\63\23\65\24\67\259\26;\27=\30?\31A\32C\33E\34G")
        buf.write("\35I\36K\37M O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61")
        buf.write("q\62s\63u\64w\65y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087")
        buf.write("=\3\2\r\3\2\62;\4\2GGgg\4\2--//\5\2C\\aac|\3\2\63;\t\2")
        buf.write("$$^^ddhhppttvv\6\2\n\f\16\17$$^^\6\2\62;C\\aac|\4\2\f")
        buf.write("\f\17\17\5\2\13\f\17\17\"\"\t\2))^^ddhhppttvv\2\u01e3")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\3\u0089\3\2\2\2\5\u008b\3\2\2\2\7\u0094\3\2\2\2\t\u0096")
        buf.write("\3\2\2\2\13\u0098\3\2\2\2\r\u009a\3\2\2\2\17\u009f\3\2")
        buf.write("\2\2\21\u00a1\3\2\2\2\23\u00b9\3\2\2\2\25\u00c9\3\2\2")
        buf.write("\2\27\u00cf\3\2\2\2\31\u00d1\3\2\2\2\33\u00db\3\2\2\2")
        buf.write("\35\u00dd\3\2\2\2\37\u00df\3\2\2\2!\u00e1\3\2\2\2#\u00e3")
        buf.write("\3\2\2\2%\u00e5\3\2\2\2\'\u00e7\3\2\2\2)\u00e9\3\2\2\2")
        buf.write("+\u00eb\3\2\2\2-\u00ed\3\2\2\2/\u00ef\3\2\2\2\61\u00f4")
        buf.write("\3\2\2\2\63\u00fa\3\2\2\2\65\u0102\3\2\2\2\67\u0105\3")
        buf.write("\2\2\29\u010a\3\2\2\2;\u0110\3\2\2\2=\u0116\3\2\2\2?\u011a")
        buf.write("\3\2\2\2A\u0123\3\2\2\2C\u0126\3\2\2\2E\u012e\3\2\2\2")
        buf.write("G\u0135\3\2\2\2I\u013c\3\2\2\2K\u0141\3\2\2\2M\u0147\3")
        buf.write("\2\2\2O\u014c\3\2\2\2Q\u0150\3\2\2\2S\u0159\3\2\2\2U\u015c")
        buf.write("\3\2\2\2W\u0164\3\2\2\2Y\u016a\3\2\2\2[\u0171\3\2\2\2")
        buf.write("]\u0173\3\2\2\2_\u0175\3\2\2\2a\u0177\3\2\2\2c\u0179\3")
        buf.write("\2\2\2e\u017b\3\2\2\2g\u017d\3\2\2\2i\u0180\3\2\2\2k\u0183")
        buf.write("\3\2\2\2m\u0186\3\2\2\2o\u0189\3\2\2\2q\u018b\3\2\2\2")
        buf.write("s\u018e\3\2\2\2u\u0190\3\2\2\2w\u0193\3\2\2\2y\u0195\3")
        buf.write("\2\2\2{\u0198\3\2\2\2}\u01a6\3\2\2\2\177\u01b2\3\2\2\2")
        buf.write("\u0081\u01b8\3\2\2\2\u0083\u01c0\3\2\2\2\u0085\u01c9\3")
        buf.write("\2\2\2\u0087\u01d5\3\2\2\2\u0089\u008a\t\2\2\2\u008a\4")
        buf.write("\3\2\2\2\u008b\u008d\t\3\2\2\u008c\u008e\t\4\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0090\3\2\2\2")
        buf.write("\u008f\u0091\t\2\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3")
        buf.write("\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\6")
        buf.write("\3\2\2\2\u0094\u0095\t\5\2\2\u0095\b\3\2\2\2\u0096\u0097")
        buf.write("\t\6\2\2\u0097\n\3\2\2\2\u0098\u0099\7$\2\2\u0099\f\3")
        buf.write("\2\2\2\u009a\u009b\7^\2\2\u009b\u009c\t\7\2\2\u009c\16")
        buf.write("\3\2\2\2\u009d\u00a0\n\b\2\2\u009e\u00a0\5\r\7\2\u009f")
        buf.write("\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\20\3\2\2\2\u00a1")
        buf.write("\u00a5\7\60\2\2\u00a2\u00a4\t\2\2\2\u00a3\u00a2\3\2\2")
        buf.write("\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6")
        buf.write("\3\2\2\2\u00a6\22\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00ac")
        buf.write("\5\t\5\2\u00a9\u00ab\5\3\2\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00b5\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\7")
        buf.write("a\2\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b4\5\3\2\2\u00b3\u00b0\3\2\2\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00ba\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\7")
        buf.write("\62\2\2\u00b9\u00a8\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bc\b\n\2\2\u00bc\24\3\2\2\2\u00bd")
        buf.write("\u00be\5\23\n\2\u00be\u00bf\5\21\t\2\u00bf\u00ca\3\2\2")
        buf.write("\2\u00c0\u00c2\5\23\n\2\u00c1\u00c3\5\21\t\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c5\5\5\3\2\u00c5\u00ca\3\2\2\2\u00c6\u00c7\5\21\t")
        buf.write("\2\u00c7\u00c8\5\5\3\2\u00c8\u00ca\3\2\2\2\u00c9\u00bd")
        buf.write("\3\2\2\2\u00c9\u00c0\3\2\2\2\u00c9\u00c6\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cc\b\13\3\2\u00cc\26\3\2\2\2\u00cd")
        buf.write("\u00d0\5I%\2\u00ce\u00d0\59\35\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\30\3\2\2\2\u00d1\u00d5\5\13\6\2\u00d2")
        buf.write("\u00d4\5\17\b\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2")
        buf.write("\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8")
        buf.write("\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\5\13\6\2\u00d9")
        buf.write("\u00da\b\r\4\2\u00da\32\3\2\2\2\u00db\u00dc\7*\2\2\u00dc")
        buf.write("\34\3\2\2\2\u00dd\u00de\7+\2\2\u00de\36\3\2\2\2\u00df")
        buf.write("\u00e0\7]\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7_\2\2\u00e2")
        buf.write("\"\3\2\2\2\u00e3\u00e4\7\60\2\2\u00e4$\3\2\2\2\u00e5\u00e6")
        buf.write("\7.\2\2\u00e6&\3\2\2\2\u00e7\u00e8\7=\2\2\u00e8(\3\2\2")
        buf.write("\2\u00e9\u00ea\7<\2\2\u00ea*\3\2\2\2\u00eb\u00ec\7}\2")
        buf.write("\2\u00ec,\3\2\2\2\u00ed\u00ee\7\177\2\2\u00ee.\3\2\2\2")
        buf.write("\u00ef\u00f0\7c\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7v")
        buf.write("\2\2\u00f2\u00f3\7q\2\2\u00f3\60\3\2\2\2\u00f4\u00f5\7")
        buf.write("d\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8")
        buf.write("\7c\2\2\u00f8\u00f9\7m\2\2\u00f9\62\3\2\2\2\u00fa\u00fb")
        buf.write("\7d\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\64\3\2\2\2\u0102\u0103\7f\2\2\u0103\u0104")
        buf.write("\7q\2\2\u0104\66\3\2\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\u0108\7u\2\2\u0108\u0109\7g\2\2\u01098\3")
        buf.write("\2\2\2\u010a\u010b\7h\2\2\u010b\u010c\7c\2\2\u010c\u010d")
        buf.write("\7n\2\2\u010d\u010e\7u\2\2\u010e\u010f\7g\2\2\u010f:\3")
        buf.write("\2\2\2\u0110\u0111\7h\2\2\u0111\u0112\7n\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7c\2\2\u0114\u0115\7v\2\2\u0115<\3")
        buf.write("\2\2\2\u0116\u0117\7h\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119>\3\2\2\2\u011a\u011b\7h\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7p\2\2\u011d\u011e\7e\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7k\2\2\u0120\u0121\7q\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122@\3\2\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7h\2\2\u0125B\3\2\2\2\u0126\u0127\7k\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7v\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7i\2\2\u012b\u012c\7g\2\2\u012c\u012d\7t\2\2\u012dD\3")
        buf.write("\2\2\2\u012e\u012f\7t\2\2\u012f\u0130\7g\2\2\u0130\u0131")
        buf.write("\7v\2\2\u0131\u0132\7w\2\2\u0132\u0133\7t\2\2\u0133\u0134")
        buf.write("\7p\2\2\u0134F\3\2\2\2\u0135\u0136\7u\2\2\u0136\u0137")
        buf.write("\7v\2\2\u0137\u0138\7t\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7p\2\2\u013a\u013b\7i\2\2\u013bH\3\2\2\2\u013c\u013d")
        buf.write("\7v\2\2\u013d\u013e\7t\2\2\u013e\u013f\7w\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140J\3\2\2\2\u0141\u0142\7y\2\2\u0142\u0143")
        buf.write("\7j\2\2\u0143\u0144\7k\2\2\u0144\u0145\7n\2\2\u0145\u0146")
        buf.write("\7g\2\2\u0146L\3\2\2\2\u0147\u0148\7x\2\2\u0148\u0149")
        buf.write("\7q\2\2\u0149\u014a\7k\2\2\u014a\u014b\7f\2\2\u014bN\3")
        buf.write("\2\2\2\u014c\u014d\7q\2\2\u014d\u014e\7w\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014fP\3\2\2\2\u0150\u0151\7e\2\2\u0151\u0152")
        buf.write("\7q\2\2\u0152\u0153\7p\2\2\u0153\u0154\7v\2\2\u0154\u0155")
        buf.write("\7k\2\2\u0155\u0156\7p\2\2\u0156\u0157\7w\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158R\3\2\2\2\u0159\u015a\7q\2\2\u015a\u015b")
        buf.write("\7h\2\2\u015bT\3\2\2\2\u015c\u015d\7k\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015e\u015f\7j\2\2\u015f\u0160\7g\2\2\u0160\u0161")
        buf.write("\7t\2\2\u0161\u0162\7k\2\2\u0162\u0163\7v\2\2\u0163V\3")
        buf.write("\2\2\2\u0164\u0165\7c\2\2\u0165\u0166\7t\2\2\u0166\u0167")
        buf.write("\7t\2\2\u0167\u0168\7c\2\2\u0168\u0169\7{\2\2\u0169X\3")
        buf.write("\2\2\2\u016a\u016e\t\5\2\2\u016b\u016d\t\t\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016fZ\3\2\2\2\u0170\u016e\3\2\2\2\u0171")
        buf.write("\u0172\7-\2\2\u0172\\\3\2\2\2\u0173\u0174\7/\2\2\u0174")
        buf.write("^\3\2\2\2\u0175\u0176\7,\2\2\u0176`\3\2\2\2\u0177\u0178")
        buf.write("\7\61\2\2\u0178b\3\2\2\2\u0179\u017a\7\'\2\2\u017ad\3")
        buf.write("\2\2\2\u017b\u017c\7#\2\2\u017cf\3\2\2\2\u017d\u017e\7")
        buf.write("(\2\2\u017e\u017f\7(\2\2\u017fh\3\2\2\2\u0180\u0181\7")
        buf.write("~\2\2\u0181\u0182\7~\2\2\u0182j\3\2\2\2\u0183\u0184\7")
        buf.write("?\2\2\u0184\u0185\7?\2\2\u0185l\3\2\2\2\u0186\u0187\7")
        buf.write("#\2\2\u0187\u0188\7?\2\2\u0188n\3\2\2\2\u0189\u018a\7")
        buf.write(">\2\2\u018ap\3\2\2\2\u018b\u018c\7>\2\2\u018c\u018d\7")
        buf.write("?\2\2\u018dr\3\2\2\2\u018e\u018f\7@\2\2\u018ft\3\2\2\2")
        buf.write("\u0190\u0191\7@\2\2\u0191\u0192\7?\2\2\u0192v\3\2\2\2")
        buf.write("\u0193\u0194\7?\2\2\u0194x\3\2\2\2\u0195\u0196\7<\2\2")
        buf.write("\u0196\u0197\7<\2\2\u0197z\3\2\2\2\u0198\u0199\7\61\2")
        buf.write("\2\u0199\u019a\7,\2\2\u019a\u019e\3\2\2\2\u019b\u019d")
        buf.write("\13\2\2\2\u019c\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a1\u01a2\7,\2\2\u01a2\u01a3\7")
        buf.write("\61\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\b>\5\2\u01a5|")
        buf.write("\3\2\2\2\u01a6\u01a7\7\61\2\2\u01a7\u01a8\7\61\2\2\u01a8")
        buf.write("\u01ac\3\2\2\2\u01a9\u01ab\n\n\2\2\u01aa\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0")
        buf.write("\b?\5\2\u01b0~\3\2\2\2\u01b1\u01b3\t\13\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\b@\5\2")
        buf.write("\u01b7\u0080\3\2\2\2\u01b8\u01ba\7\62\2\2\u01b9\u01bb")
        buf.write("\5\3\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\bA\6\2\u01bf\u0082\3\2\2\2\u01c0\u01c4\7")
        buf.write("$\2\2\u01c1\u01c3\5\17\b\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\bB\7\2")
        buf.write("\u01c8\u0084\3\2\2\2\u01c9\u01cd\7$\2\2\u01ca\u01cc\5")
        buf.write("\17\b\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d0\3\2\2\2")
        buf.write("\u01cf\u01cd\3\2\2\2\u01d0\u01d1\7^\2\2\u01d1\u01d2\n")
        buf.write("\f\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\bC\b\2\u01d4\u0086")
        buf.write("\3\2\2\2\u01d5\u01d6\13\2\2\2\u01d6\u01d7\bD\t\2\u01d7")
        buf.write("\u0088\3\2\2\2\26\2\u008d\u0092\u009f\u00a5\u00ac\u00b0")
        buf.write("\u00b5\u00b9\u00c2\u00c9\u00cf\u00d5\u016e\u019e\u01ac")
        buf.write("\u01b4\u01bc\u01c4\u01cd\n\3\n\2\3\13\3\3\r\4\b\2\2\3")
        buf.write("A\5\3B\6\3C\7\3D\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_LIT = 1
    FLOAT_LIT = 2
    BOOL_LIT = 3
    STRING_LIT = 4
    LB = 5
    RB = 6
    LSB = 7
    RSB = 8
    DOT = 9
    COMMA = 10
    SEMI = 11
    COLON = 12
    LCB = 13
    RCB = 14
    AUTO = 15
    BREAK = 16
    BOOLEAN = 17
    DO = 18
    ELSE = 19
    FALSE = 20
    FLOAT = 21
    FOR = 22
    FUNC = 23
    IF = 24
    INT = 25
    RETURN = 26
    STR = 27
    TRUE = 28
    WHILE = 29
    VOID = 30
    OUT = 31
    CONTINUE = 32
    OF = 33
    INHERIT = 34
    ARRAY = 35
    IDENTIFIER = 36
    ADD = 37
    SUB = 38
    MUL = 39
    DIV = 40
    MOD = 41
    NOT = 42
    AND = 43
    OR = 44
    EQUAL = 45
    NOT_EQUAL = 46
    SMALLER = 47
    SMALLER_OR_EQUAL = 48
    BIGGER = 49
    BIGGER_OR_EQUAL = 50
    ASSIGN = 51
    DOUBLECOLON = 52
    COMMENT_BLOCK = 53
    COMMENT_LINE = 54
    WS = 55
    ERROR_0 = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "LB", "RB", 
            "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNC", "IF", "INT", "RETURN", "STR", "TRUE", "WHILE", 
            "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "IDENTIFIER", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "NOT_EQUAL", "SMALLER", "SMALLER_OR_EQUAL", "BIGGER", "BIGGER_OR_EQUAL", 
            "ASSIGN", "DOUBLECOLON", "COMMENT_BLOCK", "COMMENT_LINE", "WS", 
            "ERROR_0", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "DIGIT", "EXPPART", "NonDigit", "NonZeroDigit", "DoubleQuote", 
                  "ESCAPE_SEQUENCE", "CHARLIT", "DECPART", "INT_LIT", "FLOAT_LIT", 
                  "BOOL_LIT", "STRING_LIT", "LB", "RB", "LSB", "RSB", "DOT", 
                  "COMMA", "SEMI", "COLON", "LCB", "RCB", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNC", 
                  "IF", "INT", "RETURN", "STR", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "IDENTIFIER", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "NOT_EQUAL", "SMALLER", "SMALLER_OR_EQUAL", "BIGGER", 
                  "BIGGER_OR_EQUAL", "ASSIGN", "DOUBLECOLON", "COMMENT_BLOCK", 
                  "COMMENT_LINE", "WS", "ERROR_0", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.INT_LIT_action 
            actions[9] = self.FLOAT_LIT_action 
            actions[11] = self.STRING_LIT_action 
            actions[63] = self.ERROR_0_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = self.text.replace("_","")
            	
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		self.text = self.text[1:-1]
            	
     

    def ERROR_0_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken('0')
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace('"','',1)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text.replace('"','',1)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


