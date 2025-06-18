letter  = ''' Dear <|name|>,
              you are selected!
              <|date|> '''

print(letter.replace("<|name|>", "Swetang").replace("<|date|>", "01/01/2023"))

