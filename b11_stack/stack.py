# stack empty
stack_empty = []

# stack with elements
# stack = ["element1", "element2", "element3", "element4", "element5", "element6", "element7", "element8"]

stack = []

# push (thêm phần tử vào stack)
# cú pháp: tên_stack.append("element")
stack.append("element1") # nằm ở đáy stack
stack.append("element2") 
stack.append("element3")
stack.append("element4")
stack.append("element5")
stack.append("element6")
stack.append("element7")
stack.append("element8") # nằm ở đỉnh stack
print(stack)

# peek (xem phần tử ở đỉnh của stack)
# cú pháp: tên_stack[-1]
print(stack[-1])
print(stack[-2])

# pop (lấy phần tử ở đỉnh stack ra)
# cú pháp: tên_stack.pop()
stack.pop() # lấy phần tử ở đỉnh stack ra và xóa nó khỏi stack
print(stack)


# back_stack = []
# search google.com (push)
# search youtube.com (push)
# search facebook.com (push)

# back_stack = ["google.com", "youtube.com", "facebook.com"]

# back (quay lại trang trước đó)
# -> youtube.com
# print("redirect to: ", facebook.com)
# print("cannot back, because back_stack is empty")

# forward (tiến về trang sau đó)
# -> facebook.com

browser = Browser()
browser.visit_page("google.com") # welcome to google.com
browser.visit_page("youtube.com") # welcome to youtube.com
browser.visit_page("facebook.com") # welcome to facebook.com

browser.back() # quay lại youtube.com
browser.back() # quay lại google.com
browser.back() # cannot back, because back_stack is empty

browser.forward() # tiến về youtube.com
browser.forward() # tiến về facebook.com
browser.forward() # cannot forward, because forward_stack is empty