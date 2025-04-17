def count_a(text):
  count = 0
  for c in text:
    if c == 'a' or c == 'A':
      count += 1
  return count
