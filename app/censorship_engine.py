def censor_text(usrtxt):
  with open("swearWords.txt") as fobj:
    swearWordstxt = fobj.read()
    profane_terms = swearWordstxt.split()
  censored_text = usrtxt
  for term in profane_terms:
    location = censored_text.find(term)
    if location == -1:
      continue
    else:
      lot = len(term)
      censored_text = censored_text.replace(term, '####')
  return censored_text