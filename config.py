DEBUG_STATEMENTS_COMMENTS_REGEX = "\".*LLVM_DEBUG.*\"|\".*debug.*\"|\".*llvm.dbg.*\"|\".*getDebugLoc\(\).*\""
ASSERT_STATEMENTS_COMMENTS_REGEX = "\".*ASSERT.*\"|\".*EXPECT.*\"|\".*@test.*\""
ASSERT_STATEMENT_REGEX = "^(\s+)?(EXPECT_|ASSERT|.*@test)"
COMMENTS_REGEX = "^(\s+)?(\#|\/\/|\/\*|.*\*\/)"
DEBUG_STATEMENTS_REGEX = "^(\s+)?(\!)?(LLVM_DEBUG|^LLVM_DEBUG|.*(@)?llvm.dbg|.*getDebugLoc\(\))"
DIRECTORIES = ['test', 'unittests']
IGNORE_EXTENSIONS = ['.rst', '.txt', '.rmd', '.TXT', '.pack', 'README', '.idx', '.md',
                     '.png', '.csv']
IGNORE_FOLDERS = "(test)|(unittests|README|.git|PAT|.idea|.gitignore|.gitattributes)"
REGRESSION_INCLUDE_EXTENSIONS = ['.cpp', '.ll', '.test', '.py']