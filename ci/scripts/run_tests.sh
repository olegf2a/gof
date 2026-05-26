#!/usr/bin/env bash
set -e

echo "🧪 Running tests for all design patterns..."

total_tests=0
failed_patterns=""

for dir in */*/; do
  if [ -d "${dir}tests" ]; then
    pattern_name=${dir%/}
    echo "🔍 Testing $pattern_name pattern..."

    for test_file in ${dir}tests/test_*.py; do
      if [ -f "$test_file" ]; then
        module=$(echo "$test_file" | sed 's|/|.|g' | sed 's|\.py$||')

        if output=$(python -m "$module" -v 2>&1); then
          test_count=$(echo "$output" | grep -o "Ran [0-9]* test" | grep -o "[0-9]*" || echo "1")
          echo "   ✅ $test_count tests passed ($module)"
          total_tests=$((total_tests + test_count))
        else
          echo "   ❌ Tests failed ($module)"
          echo "$output" | grep -E "(FAIL|ERROR|Traceback|ModuleNotFoundError|ImportError|AssertionError)" | sed 's/^/      /'
          echo "   --- Full output ---"
          echo "$output" | sed 's/^/      /'
          failed_patterns="$failed_patterns $pattern_name"
        fi
      fi
    done
  fi
done

echo ""
echo "📊 Total: $total_tests tests"

if [ -n "$failed_patterns" ]; then
  echo "❌ Failed:$failed_patterns"
  exit 1
else
  echo "✅ All tests passed!"
fi
