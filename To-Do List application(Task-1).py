import tkinter as tk
from tkinter import messagebox

Tasks_list = []   

def addTask():
    taskName = task_name.get()
    if taskName.strip() == "":
        messagebox.showwarning("Warning", " ! Empty Task Field ! ")
        return
    Tasks_list.append({"name": taskName, "status": "❌"})
    displayTask()
    task_name.delete(0, tk.END)
    print(f"---- Task {taskName} is Added Successfully ------")
    
def markTask():
    index = int(index_num.get())-1
    statusMark = status_mark.get()
    
    if index < 0 or index >= len(Tasks_list):
        messagebox.showwarning("Warning", " ! You Must Enter The Index Of The Task! ")
        return
    
    statusMark = statusMark.strip()
    
    if (statusMark.lower() == "done"):
        Tasks_list[index]["status"] = "✔️"
        print(f"---- Task mark as {statusMark} Successfully ------")
    elif (statusMark.lower() == "pending"):
        Tasks_list[index]["status"] = "❌"
        print(f"---- Task mark as {statusMark} Successfully ------")
    else:
        messagebox.showwarning("Warning", " Empty Field! OR write on [done / pending]")
    displayTask()
    index_num.delete(0, tk.END)
    status_mark.delete(0, tk.END)
            
def updateTask():
    index = int(index_num.get())-1
    newTaskName = task_name.get()
    statusMark = status_mark.get()
    
    if index < 0 or index >= len(Tasks_list):
        messagebox.showwarning("Warning", " ! You Must Enter The Index Of The Task! ")
        return
    if newTaskName.strip() == "" or statusMark.strip() == "":
        messagebox.showwarning("Warning", " ! EMPTY FIELD DETECTED ! ")
        return
    
    Tasks_list[index]["name"] = newTaskName
    if (statusMark.lower() == "done"):
        Tasks_list[index]["status"] = "✔️"
        print(f"---- Task mark as {statusMark} Successfully ------")
    elif (statusMark.lower() == "pending"):
        Tasks_list[index]["status"] = "❌"
        print(f"---- Task mark as {statusMark} Successfully ------")
    else:
        messagebox.showwarning("Warning", " Empty Field! OR write on [done / pending]")
    displayTask()
    task_name.delete(0, tk.END)
    index_num.delete(0, tk.END)
    status_mark.delete(0, tk.END)
    print(f"---- Task {newTaskName} is Updated Successfully ------")
       
def deleteTask():
    index = int(index_num.get())-1
    if index < 0 or index >= len(Tasks_list):
        messagebox.showwarning("Warning", " ! You Must Enter The Index Of The Task! ")
        return
    Tasks_list.pop(index)
    displayTask()
    print("---- Task is deleted Successfully ------")
    
def displayTask():
        listField.delete(0, tk.END)
        i = 1
        for task in Tasks_list:
            listField.insert(tk.END, f" {i}.> {task['name']} [{task['status']}]")
            i+=1

root = tk.Tk()
root.title("TO-DO LIST APPLICATION")
root.geometry("410x820")
root.config(bg = "#0f1117")

tk.Label(root, text= "📋 TO-DO LIST APPLICATION ", font=("Georgia", 20, "bold"), bg="#394142", fg="#f0c040", width=40).pack(pady=10)
tk.Label(root, text = """
🤏 Instruction:\n
    1.) To Add Task fill only 'Task field'.
    2.) To Mark task fill 'Mark' & 'number' field.
    3.) To Update task fill all of them.
    4.) To delete task fill only "number" filed.
         """, font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040", justify="left").pack()

tk.Label(root, text = "Enter Task Name", font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040",).pack()
task_name = tk.Entry(root,font=("Courier", 13), bg="#252836", fg="#f0f0f0", width=30, bd=0,)
task_name.pack(pady=10, ipady=5)

tk.Label(root, text = "Enter status (done / pending)", font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040",).pack()
status_mark = tk.Entry(root,font=("Courier", 13), bg="#252836", fg="#f0f0f0", width=30, bd=0)
status_mark.pack(pady=10, ipady=5)

tk.Label(root, text = "Enter Task number(1/2...)", font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040",).pack()
index_num = tk.Entry(root,font=("Courier", 13), bg="#252836", fg="#f0f0f0", width=30, bd = 0)
index_num.pack(pady=10, ipady=5)

tk.Button(root, text="Add Task", font=("Georgia", 10, "bold"), bg = "#f0c040", fg= "white",width=20, command=addTask).pack(pady=5,ipady=5)
tk.Button(root, text="Mark Task", width=20, font=("Georgia", 10, "bold"), bg = "#f0c040", fg= "white", command=markTask).pack(pady=5, ipady=5)
tk.Button(root, text="Update Task", font=("Georgia", 10, "bold"), bg = "#f0c040", fg= "white", width=20, command=updateTask).pack(pady=5,ipady=5)
tk.Button(root, text="Delete Task", font=("Georgia", 10, "bold"), bg = "#f0c040", fg= "white", width=20, command=deleteTask).pack(pady=5,ipady=5)

listField = tk.Listbox(root, font=("Georgia", 12, "bold"), bg = "#394142", fg= "white", width=40, height=15)
listField.pack(pady=10)

root.mainloop()
             