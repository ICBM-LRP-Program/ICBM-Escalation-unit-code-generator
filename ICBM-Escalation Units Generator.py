#全局设置
import tkinter as tk
from tkinter import ttk
from tkinter import END
from tkinter.ttk import Combobox
from tkinter import messagebox



def main():
    root = tk.Tk()
    root.title("ICBM: Escalation Unit Generator")

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=10, pady=10) 

###test
### 2025/10/10-15:43



#    # 更清晰的balloon函数版本
#    def addBalloon(widget, text):
#        balloon_ref = [None]  # 使用列表引用保持状态
#
#        def showBalloon(event):
#            if balloon_ref[0]:
#                balloon_ref[0].destroy()
#            balloon_ref[0] = tk.Toplevel(widget, bg='lightyellow', relief='solid', borderwidth=1)
#            balloon_ref[0].wm_overrideredirect(1)
#            x = widget.winfo_rootx() + widget.winfo_width() // 2 - 100
#            y = widget.winfo_rooty() + widget.winfo_height() + 5
#            balloon_ref[0].wm_geometry(f"+{x}+{y}")
#            label = tk.Label(
#            balloon_ref[0], 
#            text=text, 
#            bg='lightyellow', 
#            padx=8, 
#            pady=4, 
#            justify='left', 
#            anchor='w',
#            wraplength=350  # 设置自动换行宽度
#            )
#            label.pack(fill='x')
#
#        def hideBalloon(event):
#            if balloon_ref[0]:
#                balloon_ref[0].destroy()
#                balloon_ref[0] = None
#
#        widget.bind("<Enter>", showBalloon)
#        widget.bind("<Leave>", hideBalloon)







    #基本信息标签页
    Frame1 = ttk.Frame(notebook)
    notebook.add(Frame1, text="基本信息和数据")

    basicInfo = ttk.Labelframe(Frame1, text="基础数据")
    basicInfo.place(x=10, y=10, width=975, height=300)





    ### 基础数据第一列
    globalNameEntry = tk.StringVar()
    techEntry = tk.StringVar()
    movieEntry = tk.StringVar()
    abstractMovieEntry = tk.StringVar()
    modelEntry = tk.StringVar()
    iconEntry = tk.StringVar()
    roundIconEntry = tk.StringVar()
    launchMePathIconEntry = tk.StringVar()

    
    # 列表字典，分别是{提示文本，输入框变量}
    colBasicInfo1 = [
        ("全局名称:", globalNameEntry),
        ("科技和描述引用:", techEntry),
        ("俯视图文件路径:", movieEntry),
        ("缩略图文件路径:", abstractMovieEntry),
        ("3D模型文件路径:", modelEntry),
        ("图标文件路径:", iconEntry),
        ("圆形图标文件路径:", roundIconEntry),
        ("发射路径图标路径:", launchMePathIconEntry)
    ]

    for i, (text, entryVar) in enumerate(colBasicInfo1):
        x = 25
        y = 10+30*i
        width = 75
        # x即该列x坐标起始点位置，y为每行y坐标起始点位置
        ttk.Label(basicInfo, text=text).grid(row=i, column=0, padx=15, pady=5, sticky="w")
        colPropertyEntry1 = ttk.Entry(basicInfo, textvariable=entryVar, width=width)
        colPropertyEntry1.grid(row=i, column=1, padx=15, pady=5, )#sticky="w")


    ### 基础数据第二列
    typeEntry = tk.StringVar()
    crashEntry = tk.StringVar()
    classEntry = tk.StringVar()
    drawSizeEntry = tk.StringVar()
    abstractDrawSizeEntry = tk.StringVar()
    soundEntry = tk.StringVar()
    launchMeSoundEntry = tk.StringVar()
    iconIDXEntry = tk.StringVar()
    
    # 列表字典，分别是{提示文本，输入框变量，宽度}
    colBasicInfo2 = [
        ("单位类型:", typeEntry, 18, "type"),
        ("爆炸效果:", crashEntry, 18, "crash"),
        ("单位分组:", classEntry, 20, "normal"),
        ("模型大小:", drawSizeEntry, 20, "normal"),
        ("缩略图尺寸:", abstractDrawSizeEntry, 20, "normal"),
        ("声音及音量:", soundEntry, 20, "normal"),
        ("发射音效:", launchMeSoundEntry, 20, "normal"),
        ("IconIDX:", iconIDXEntry, 20, "normal"),

    ]

    for i, (text, entryVar, width, type) in enumerate(colBasicInfo2):
        x = 515
        y = 10+30*i
        if type == "normal":
        # x即该列x坐标起始点位置，y为每行y坐标起始点位置
            ttk.Label(basicInfo, text=text).grid(row=i, column=2, padx=15, pady=5, sticky="w")
            ttk.Entry(basicInfo, textvariable=entryVar, width=width).grid(row=i, column=3, padx=15, pady=5)
        if type == "type":
            ttk.Label(basicInfo, text=text).grid(row=i, column=2, padx=15, pady=5, sticky="w")
            ttk.Combobox(basicInfo, values=["Ground", "Airborne", "Naval", "Subwater", "Satellite"], textvariable=typeEntry, width=width).grid(row=i, column=3, padx=15, pady=5)

        if type == "crash":
            ttk.Label(basicInfo, text=text).grid(row=i, column=2, padx=15, pady=5, sticky="w")
            ttk.Combobox(basicInfo, values=["std_bomb", "big_bomb"], textvariable=entryVar, width=width).grid(row=i, column=3, padx=15, pady=5)







    propertyInfo = ttk.Labelframe(Frame1, text="属性数据")
    propertyInfo.place(x=10, y=320, width=530, height=360)

    ### 第一列
    # 定义变量
    powerEntry = tk.StringVar()
    turnSpeedEntry = tk.StringVar()
    speedEntry = tk.StringVar()
    rangeEntry = tk.StringVar()
    sizeEntry = tk.StringVar()
    productionCostEntry = tk.StringVar()
    selfDestructTimeEntry = tk.StringVar()
    autoRepairEntry = tk.StringVar()
    resupplyRangeEntry = tk.StringVar()
    maxAutoEngageRangeEntry = tk.StringVar()
    followRadiusEntry = tk.StringVar()
    occupationRadiusEntry = tk.StringVar()
    maxElevationEntry = tk.StringVar()
    minElevationEntry = tk.StringVar()
    productionPlacementRadiusEntry = tk.StringVar()
    drawOrderEntry = tk.StringVar()
    maxNumberOnMapEntry = tk.StringVar()
    maxNumberToOrderEntry = tk.StringVar()
    hangarSpaceRequiredEntry = tk.StringVar()
    hangarMaxLoadEntry = tk.StringVar()

    # 列表字典，分别是{提示文本，输入框变量}
    colProperty1 = [
        ("生命值:", powerEntry),
        ("转向速度:", turnSpeedEntry),
        ("移动速度:", speedEntry),
        ("最大航程:", rangeEntry),
        ("受击体积:", sizeEntry),
        ("生产成本:", productionCostEntry),
        ("自毁时间:", selfDestructTimeEntry),
        ("自修复系数:", autoRepairEntry),
        ("补给范围:", resupplyRangeEntry),
        ("自动交战范围:", maxAutoEngageRangeEntry)
        ]

    for i, (text, entryVar) in enumerate(colProperty1):
        # x即该列x坐标起始点位置，y为每行y坐标起始点位置， width为输入框宽度
        x = 25
        y = 5+30*i
        width = 15
        ttk.Label(propertyInfo, text=text).grid(row=i, column=0, padx=15, pady=5, sticky="w")
        colPropertyEntry1 = ttk.Entry(propertyInfo, textvariable=entryVar, width=width)
        colPropertyEntry1.grid(row=i, column=1, padx=15, pady=5)


    ### 第二列


    colProperty2 = [
        ("其他单位跟随半径:", followRadiusEntry),
        ("占领范围半径:", occupationRadiusEntry),
        ("最高高度:", maxElevationEntry),
        ("最低高度:", minElevationEntry),
        ("周围可放置范围:", productionPlacementRadiusEntry),
        ("缩略图绘制顺序:", drawOrderEntry),
        ("最大放置数量:", maxNumberOnMapEntry),
        ("最大拥有数量:", maxNumberToOrderEntry),
        ("容量需求:", hangarSpaceRequiredEntry),
        ("单位容量:", hangarMaxLoadEntry)
    ]

    for i, (text, entryVar) in enumerate(colProperty2):
        x = 200
        y = 5+30*i
        width = 15
        ttk.Label(propertyInfo, text=text).grid(row=i, column=2, padx=15, pady=5, sticky="w")
        colPropertyEntry2 = ttk.Entry(propertyInfo, textvariable=entryVar, width=width)
        colPropertyEntry2.grid(row=i, column=3, padx=15, pady=5)




    customParameters = ttk.Labelframe(Frame1, text="自定义参数")
    customParameters.place(x=550, y=320, width=435, height=360)
    
    customTableData = tk.StringVar()

    def add_to_table():
        if customEntry1.get().strip():
            customTable.insert("", tk.END, values=(customEntry1.get(), customEntry2.get()))
            customEntry1.delete(0, tk.END)
            customEntry2.delete(0, tk.END)

    def delete_selected():
        if customTable.selection():
            customTable.delete(customTable.selection()[0])

    def print_table():
        items = customTable.get_children()
        if not items:
            print("表格为空")
            customTableData.set("")
            return ""
        table_data = ""
        for item in items:
            values = customTable.item(item, 'values')
            if values:
                table_data += f"    {values[0]} {values[1]}\n"
        customTableData.set(table_data)
        print(customTableData.get())
        return table_data


    def map_to_entries():
        selected = customTable.selection()
        if selected:
            values = customTable.item(selected[0], 'values')
            customEntry1.delete(0, tk.END)
            customEntry2.delete(0, tk.END)
            if values:
                customEntry1.insert(0, values[0])
                if len(values) > 1:
                    customEntry2.insert(0, values[1])

    def save_to_current_row():
        selected = customTable.selection()
        if not selected:
            add_to_table()  # 无选中行则添加新行
        else:
            customTable.item(selected[0], values=(customEntry1.get(), customEntry2.get()))
            customEntry1.delete(0, tk.END)
            customEntry2.delete(0, tk.END)

    # 使用grid布局管理器来避免框架互相干扰
    customSheetFrame = ttk.Frame(customParameters)
    customSheetFrame.grid(row=0, column=0, sticky="nw", padx=5, pady=5) 

    ttk.Label(customSheetFrame, text="参数:").grid(row=0, column=0, padx=5, pady=1, sticky="w")
    customEntry1 = ttk.Entry(customSheetFrame, width=20)
    customEntry1.grid(row=1, column=0, padx=5, pady=1)
    ttk.Label(customSheetFrame, text="值").grid(row=0, column=1, padx=5, pady=1, sticky="w")
    customEntry2 = ttk.Entry(customSheetFrame, width=20)
    customEntry2.grid(row=1, column=1, padx=5, pady=1)

    customTable = ttk.Treeview(customSheetFrame, columns=("col1", "col2"), show="headings", height=12)
    customTable.heading("col1", text="参数")
    customTable.heading("col2", text="值")
    customTable.column("col1", width=150)
    customTable.column("col2", width=150)
    customTable.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    customButtonFrame = ttk.Frame(customParameters)
    customButtonFrame.grid(row=0, column=1, sticky="se", padx=1, pady=5)  

    ttk.Button(customButtonFrame, text="添加至表格", command=add_to_table, width=12).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(customButtonFrame, text="删除选中行", command=delete_selected, width=12).grid(row=1, column=0, padx=5, pady=5)

    ttk.Button(customButtonFrame, text="从选中行读取", command=map_to_entries, width=12).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(customButtonFrame, text="保存至当前行", command=save_to_current_row, width=12).grid(row=3, column=0, padx=5, pady=5)

    #ttk.Button(customButtonFrame, text="debug", command=print_table, width=12).grid(row=4, column=0, padx=5, pady=5)  

    #scrollbar = ttk.Scrollbar(customSheetFrame, orient="vertical", command=table.yview)
    #table.configure(yscrollcommand=scrollbar.set)
    #scrollbar.place(x=300, y=30, height=105)























    Frame2 = ttk.Frame(notebook)
    notebook.add(Frame2, text="行为与子单位")

    behaviorCtrl = ttk.Labelframe(Frame2, text="行为控制")
    behaviorCtrl.place(x=10, y=10, width=350, height=670)


    
    #行为控制标签页

    #DecayTimer


    behaviorString = tk.StringVar()

    alwaysVisibleOnEnemyTerritoryCheckbox = tk.BooleanVar()
    doesNotTriggerWarWhenAttackedCheckbox = tk.BooleanVar()
    canCrossBorderDuringPeaceTimeCheckBox = tk.BooleanVar()
    reportAsHostedCheckBox = tk.BooleanVar()
    targetInPlannerCheckBox = tk.BooleanVar()
    canAccessGlobalStorageCheckBox = tk.BooleanVar()
    canHangInTheAirCheckBox = tk.BooleanVar()
    hideOwnershipCheckBox = tk.BooleanVar()
    canPatrolPointCheckBox = tk.BooleanVar()
    autoReturnCheckBox = tk.BooleanVar()
    doesNotTriggerWarOnAttackCheckBox = tk.BooleanVar()
    producedByAnotherUnitCheckBox = tk.BooleanVar()
    fixedRotationAngleCheckBox = tk.BooleanVar()
    attackOnMoveCheckBox = tk.BooleanVar()
    hiddenFromAlliesCheckBox = tk.BooleanVar()
    attackIfDestroyedCheckBox = tk.BooleanVar()
    attackerInPlannerCheckBox = tk.BooleanVar()
    noAutoAttackCheckBox = tk.BooleanVar()
    noAutoAttackSubCheckBox = tk.BooleanVar()
    slaveCheckBox = tk.BooleanVar()
    canAccessWeaponStockpileCheckBox = tk.BooleanVar()
    canAccessUnitStockpileCheckBox = tk.BooleanVar()
    showDisabledOnDeploymentMarkerCheckBox = tk.BooleanVar()
    destroyOnFactionSurrenderCheckBox = tk.BooleanVar()
    ass = tk.BooleanVar()


    behaviorMaps = [
        ("在敌方领土可见", "AlwaysVisibleOnEnemyTerritory", alwaysVisibleOnEnemyTerritoryCheckbox, "Boolean", "Normal"),
        ("受击不触发战争", "DoesNotTriggerWarWhenAttacked", doesNotTriggerWarWhenAttackedCheckbox, "Boolean", "HideWhenFalse"),
        ("和平时期可跨越边界", "CanCrossBorderDuringPeaceTime", canCrossBorderDuringPeaceTimeCheckBox, "Boolean", "Normal"),
        ("显示被装载于母单位", "ReportAsHosted", reportAsHostedCheckBox, "Boolean", "HideWhenFalse"),
        ("在被攻击名单中", "TargetInPlanner", targetInPlannerCheckBox, "Boolean", "HideWhenFalse"),
        ("可访问全局武库", "CanAccessGlobalStorage", canAccessGlobalStorageCheckBox, "Boolean", "Normal"),
        ("可以访问本地武库", "CanAccessWeaponStockpile", canAccessWeaponStockpileCheckBox, "Boolean", "Normal"),
        ("可以访问单位武库", "CanAccessUnitStockpile", canAccessUnitStockpileCheckBox, "Boolean", "Normal"),
        ("可悬停（空中单位）", "CanHangInTheAir", canHangInTheAirCheckBox, "Boolean", "HideWhenFalse"),
        ("隐藏所有者阵营", "HideOwnership", hideOwnershipCheckBox, "Boolean", "Normal"),
        ("可设置巡逻点", "CanPatrolPoint", canPatrolPointCheckBox, "Boolean", "HideWhenFalse"),
        ("自动返回母单位", "AutoReturn", autoReturnCheckBox, "Boolean", "HideWhenFalse"),
        ("攻击不触发战争", "DoesNotTriggerWarOnAttack", doesNotTriggerWarOnAttackCheckBox, "Boolean", "Normal"),
        ("由其他单位生产", "ProducedByAnotherUnit", producedByAnotherUnitCheckBox, "Boolean", "HideWhenFalse"),
        ("固定朝向（建筑物）", "FixedRotationAngle", fixedRotationAngleCheckBox, "Boolean", "HideWhenFalse"),
        ("移动时可攻击", "AttackOnMove", attackOnMoveCheckBox, "Boolean", "HideWhenFalse"),
        ("部署时显示禁用", "ShowDisabledOnDeploymentMarker", showDisabledOnDeploymentMarkerCheckBox, "Boolean", "HideWhenFalse"),
        ("投降后自动摧毁", "DestroyOnFactionSurrender", destroyOnFactionSurrenderCheckBox, "Boolean", "HideWhenFalse"),
        ("对盟友隐藏", "HiddenFromAllies", hiddenFromAlliesCheckBox, "Existed", "HideWhenFalse"),
        ("被摧毁时反击", "AttackIfDestroyed", attackIfDestroyedCheckBox, "Existed", "HideWhenFalse"),
        ("在攻击者名单中", "AttackerInPlanner", attackerInPlannerCheckBox, "Existed", "HideWhenFalse"),
        ("不自动攻击敌方单位", "NoAutoAttack", noAutoAttackCheckBox, "Existed", "Normal"),
        ("不自动攻击潜艇单位", "NoAutoAttackSub", noAutoAttackSubCheckBox, "Existed", "Normal"),
        ("附属于母单位", "Slave", slaveCheckBox, "Existed", "HideWhenFalse")
    ]

    def booleanCheckBoxCommand():    
        behaviorData = ""
        for i, (text, text2, Var, type, hide) in enumerate(behaviorMaps):
            if Var.get():
                if type == "Boolean":
                    behaviorData += f"    {text2} True\n"
                if type == "Existed":
                    behaviorData += f"    {text2}\n"
            else:
                if hide == "HideWhenFalse":
                    behaviorData += f""
                else:
                    behaviorData += f"    {text2} False\n"
            behaviorString.set(behaviorData)
        #print(behaviorString.get())

            

    for i, (text, text2, Var, type, hide) in enumerate(behaviorMaps):
        nextCol = 19
        if i < nextCol :
            row = i
            col = 0
        if i >= nextCol:
            row = i-nextCol
            col = 1
        if  type == "Boolean":
            ttk.Checkbutton(behaviorCtrl, text=text, variable=Var, command=booleanCheckBoxCommand).grid(row=row, column=col, padx=15, pady=5, sticky="w")
        elif type == "Existed":
            ttk.Checkbutton(behaviorCtrl, text=text, variable=Var, command=booleanCheckBoxCommand).grid(row=row, column=col, padx=15, pady=5, sticky="w")
        else:
            print("DEBUG_TPYE")



    behaviorCtrl = ttk.Labelframe(Frame2, text="允许生产的单位")
    behaviorCtrl.place(x=370, y=10, width=205, height=330)

    behaviorCtrl = ttk.Labelframe(Frame2, text="子单位")
    behaviorCtrl.place(x=585, y=10, width=400, height=330)    

    behaviorCtrl = ttk.Labelframe(Frame2, text="允许搭载的单位")
    behaviorCtrl.place(x=370, y=350, width=615, height=330)


















    #单位数据标签页
    tabUnitData = ttk.Frame(notebook)
    notebook.add(tabUnitData, text="测试2")

    #ass = tk.Label(tabUnitData, text="饿饿饿\n啊啊啊")
    #ass.pack()


















    #取消按钮
    def cancelNameString():
        askFillDefault = messagebox.askokcancel("清除当前值", "是否确认清除当前值？此操作不可撤销。")
        if askFillDefault:
            globalNameEntry.set("")
            techEntry.set("")
            movieEntry.set("")
            abstractMovieEntry.set("")
            modelEntry.set("")
            iconEntry.set("")
            roundIconEntry.set("")
            launchMePathIconEntry.set("")
            typeEntry.set("")
            crashEntry.set("")
            classEntry.set("")
            drawSizeEntry.set("")
            abstractDrawSizeEntry.set("")
            soundEntry.set("")
            launchMeSoundEntry.set("")
            iconIDXEntry.set("")
            powerEntry.set("")
            turnSpeedEntry.set("")
            speedEntry.set("")
            rangeEntry.set("")
            sizeEntry.set("")
            productionCostEntry.set("")
            selfDestructTimeEntry.set("")
            autoRepairEntry.set("")
            resupplyRangeEntry.set("")
            maxAutoEngageRangeEntry.set("")
            followRadiusEntry.set("")
            occupationRadiusEntry.set("")
            maxElevationEntry.set("")
            minElevationEntry.set("")
            productionPlacementRadiusEntry.set("")
            drawOrderEntry.set("")
            maxNumberOnMapEntry.set("")
            maxNumberToOrderEntry.set("")
            hangarSpaceRequiredEntry.set("")
            hangarMaxLoadEntry.set("")
            customTableData.set("")

            alwaysVisibleOnEnemyTerritoryCheckbox.set(False)
            doesNotTriggerWarWhenAttackedCheckbox.set(False)
            canCrossBorderDuringPeaceTimeCheckBox.set(False)
            reportAsHostedCheckBox.set(False)
            targetInPlannerCheckBox.set(False)
            canAccessGlobalStorageCheckBox.set(False)
            canHangInTheAirCheckBox.set(False)
            hideOwnershipCheckBox.set(False)
            canPatrolPointCheckBox.set(False)
            autoReturnCheckBox.set(False)
            doesNotTriggerWarOnAttackCheckBox.set(False)
            producedByAnotherUnitCheckBox.set(False)
            fixedRotationAngleCheckBox.set(False)
            attackOnMoveCheckBox.set(False)
            hiddenFromAlliesCheckBox.set(False)
            attackIfDestroyedCheckBox.set(False)
            attackerInPlannerCheckBox.set(False)
            noAutoAttackCheckBox.set(False)
            noAutoAttackSubCheckBox.set(False)
            slaveCheckBox.set(False)
            canAccessWeaponStockpileCheckBox.set(False)
            canAccessUnitStockpileCheckBox.set(False)
            showDisabledOnDeploymentMarkerCheckBox.set(False)
            destroyOnFactionSurrenderCheckBox.set(False)


            # 清空表格中的所有行
            for item in customTable.get_children():
                customTable.delete(item)
    


    #    print(globalNameEntry.get())
    #    print(techEntry.get())
    # 创建按钮容器框架


    # 使用 grid 布局让按钮在右下角横排
    

    #应用按钮
    def fillDefault():
        askFillDefault = messagebox.askokcancel("填充默认值", "是否确认填充默认值？这将覆盖当前所有输入内容，此操作不可撤销。")
        booleanCheckBoxCommand()
        if askFillDefault:
            globalNameEntry.set("U_NameExample")
            techEntry.set("T_TechExample")
            movieEntry.set("Units/Images/[Type]/Mid-Level or Topdown/Example.midx")
            abstractMovieEntry.set("Units/Images/[Type]/Abstract/Example.midx")
            modelEntry.set("Units/Images/[Type]/Example.midx")
            iconEntry.set("Units/Images/Icons/[Type]/Example.midx")
            roundIconEntry.set("Units/Images/Icons/[Type]/Example_R.midx")
            launchMePathIconEntry.set("path/launch Example")
            typeEntry.set("Ground")
            classEntry.set("UC_Ground")
            drawSizeEntry.set("25")
            abstractDrawSizeEntry.set("25")
            soundEntry.set("1024, 0.5")
            launchMeSoundEntry.set("1024")
            iconIDXEntry.set("52")

            powerEntry.set("10")
            turnSpeedEntry.set("30")
            speedEntry.set("60")
            rangeEntry.set("")
            sizeEntry.set("0.5")
            productionCostEntry.set("0.5")
            selfDestructTimeEntry.set("30")
            autoRepairEntry.set("0.01")
            resupplyRangeEntry.set("")
            maxAutoEngageRangeEntry.set("75")
            followRadiusEntry.set("20")
            occupationRadiusEntry.set("100")
            maxElevationEntry.set("")
            minElevationEntry.set("")
            productionPlacementRadiusEntry.set("")
            drawOrderEntry.set("")
            maxNumberOnMapEntry.set("5")
            maxNumberToOrderEntry.set("5")
            hangarSpaceRequiredEntry.set("1")
            hangarMaxLoadEntry.set("")

            alwaysVisibleOnEnemyTerritoryCheckbox.set(False)
            doesNotTriggerWarWhenAttackedCheckbox.set(False)
            canCrossBorderDuringPeaceTimeCheckBox.set(False)
            reportAsHostedCheckBox.set(False)
            targetInPlannerCheckBox.set(True)
            canAccessGlobalStorageCheckBox.set(False)
            canHangInTheAirCheckBox.set(False)
            hideOwnershipCheckBox.set(False)
            canPatrolPointCheckBox.set(False)
            autoReturnCheckBox.set(False)
            doesNotTriggerWarOnAttackCheckBox.set(False)
            producedByAnotherUnitCheckBox.set(False)
            fixedRotationAngleCheckBox.set(False)
            attackOnMoveCheckBox.set(False)
            hiddenFromAlliesCheckBox.set(False)
            attackIfDestroyedCheckBox.set(True)
            attackerInPlannerCheckBox.set(True)
            noAutoAttackCheckBox.set(False)
            noAutoAttackSubCheckBox.set(False)
            slaveCheckBox.set(False)
            canAccessWeaponStockpileCheckBox.set(False)
            canAccessUnitStockpileCheckBox.set(False)
            showDisabledOnDeploymentMarkerCheckBox.set(False)
            destroyOnFactionSurrenderCheckBox.set(False)
            
            # 清空表格并添加示例文本
            for item in customTable.get_children():
                customTable.delete(item)
            customTable.insert("", tk.END, values=("/TestOption1", "Value1"))
            customTable.insert("", tk.END, values=("/TestOption2", "Value2"))
            

    #生成代码按钮

    
    #生成代码段
    def generateCode():
        # 先把各项检查并生成对应的 StringVar 内容
        checkBasicData()

        if (globalNameEntry.get() == "" or
            techEntry.get() == "" or
            movieEntry.get() == "" or
            abstractMovieEntry.get() == "" or
            modelEntry.get() == "" or
            iconEntry.get() == ""):

            messagebox.showwarning("请再次检查", "请确保所有必填字段均已填写！")
            return

        # 使用 Toplevel 而不是再创建一个 Tk 实例
        outputDataWindow = tk.Toplevel(root)
        outputDataWindow.title("生成的代码")
        outputDataWindow.geometry("600x800")
        outputDataWindow.resizable(False, True)

        # 先创建滚动条，再创建 Text 并将其连接
        OPUS_Scrollbar = tk.Scrollbar(outputDataWindow, orient="vertical")
        OPUS_Scrollbar.pack(side="right", fill="y")

        OPUS = tk.Text(outputDataWindow, width=80, height=52, font=("Consolas", 10), yscrollcommand=OPUS_Scrollbar.set)
        OPUS.pack(side="left", fill="both", expand=True)

        OPUS_Scrollbar.config(command=OPUS.yview)

        # 组合输出字符串（确保使用之前调用的 checkBasicData 已填充这些 StringVar）
        outputUnitString = (
            f"{nameString.get()}"
            f"{techString.get()}"
            f"{movieString.get()}"
            f"{abstractMovieString.get()}"
            f"{modelString.get()}"
            f"{iconString.get()}"
            f"{roundIconString.get()}"
            f"{launchMePathIconString.get()}"
            f"{typeString.get()}"
            f"{classString.get()}"
            f"{drawSizeString.get()}"
            f"{abstractDrawSizeString.get()}"
            f"{soundString.get()}"
            f"{launchMeSoundString.get()}"
            f"{iconIDXString.get()}"
            f"\n"
            f"{powerString.get()}"
            f"{turnspeedString.get()}"
            f"{speedString.get()}"
            f"{rangeString.get()}"
            f"{sizeString.get()}"
            f"{productioncostString.get()}"
            f"{selfdestructtimeString.get()}"
            f"{autorepairString.get()}"
            f"{resupplyrangeString.get()}"
            f"{maxautoengagerangeString.get()}"
            f"{followradiusString.get()}"
            f"{occupationradiusString.get()}"
            f"{maxelevationString.get()}"
            f"{minelevationString.get()}"
            f"{productionplacementradiusString.get()}"
            f"{draworderString.get()}"
            f"{maxNumberOnMapString.get()}"
            f"{maxNumberToOrderString.get()}"
            f"{hangarMaxLoadString.get()}"
            f"{hangarSpaceRequiredString.get()}"
            f"{customTableData.get()}"
            f"\n"
            f"{behaviorString.get()}"
        )

        OPUS.insert(END, outputUnitString)

    

    nameString = tk.StringVar()
    techString = tk.StringVar()
    movieString = tk.StringVar()
    abstractMovieString = tk.StringVar()
    modelString = tk.StringVar()
    iconString = tk.StringVar()
    roundIconString = tk.StringVar()
    launchMePathIconString = tk.StringVar()
    typeString = tk.StringVar()
    classString = tk.StringVar()
    crashString = tk.StringVar()
    drawSizeString = tk.StringVar()
    abstractDrawSizeString = tk.StringVar()
    soundString = tk.StringVar()
    launchMeSoundString = tk.StringVar()
    iconIDXString = tk.StringVar()
    powerString = tk.StringVar()
    turnspeedString = tk.StringVar()
    speedString = tk.StringVar()
    rangeString = tk.StringVar()
    sizeString = tk.StringVar()
    productioncostString = tk.StringVar()
    selfdestructtimeString = tk.StringVar()
    autorepairString = tk.StringVar()
    resupplyrangeString = tk.StringVar()
    maxautoengagerangeString = tk.StringVar()
    followradiusString = tk.StringVar()
    occupationradiusString = tk.StringVar()
    maxelevationString = tk.StringVar()
    minelevationString = tk.StringVar()
    productionplacementradiusString = tk.StringVar()
    draworderString = tk.StringVar()
    maxNumberOnMapString = tk.StringVar()
    maxNumberToOrderString = tk.StringVar()
    hangarSpaceRequiredString = tk.StringVar()
    hangarMaxLoadString = tk.StringVar()
    


    checkMap = [
        ("Name", globalNameEntry, nameString, "Name"),
        ("Tech", techEntry, techString, "QuotedNormal"),
        ("Movie", movieEntry, movieString, "QuotedNormal"),
        ("AbstractMovie", abstractMovieEntry, abstractMovieString, "QuotedNormal"),
        ("Model", modelEntry, modelString, "QuotedNormal"),
        ("Icon", iconEntry, iconString, "QuotedNormal"),
        ("RoundIcon", roundIconEntry, roundIconString, "QuotedNormal"),
        ("LaunchMePath", launchMePathIconEntry, launchMePathIconString, "QuotedNormal"),
        
        ("Type", typeEntry, typeString, "Normal"),
        ("Crash", crashEntry, crashString, "QuotedNormal"),
        ("Class", classEntry, classString, "Normal"),
        ("DrawSize", drawSizeEntry, drawSizeString, "Normal"),
        ("AbstractDrawSize", abstractDrawSizeEntry, abstractDrawSizeString, "Normal"),
        ("Sound", soundEntry, soundString, "Sound"),
        ("LaunchMeSound", launchMeSoundEntry, launchMeSoundString, "Normal"),
        ("IconIDX", iconIDXEntry, iconIDXString, "Normal"),
        ("Power", powerEntry, powerString, "Normal"),
        ("TurnSpeed", turnSpeedEntry, turnspeedString, "Normal"),
        ("Speed", speedEntry, speedString, "Normal"),
        ("Range", rangeEntry, rangeString, "Normal"),
        ("Size", sizeEntry, sizeString, "Normal"),
        ("ProductionCost", productionCostEntry, productioncostString, "Normal"),
        ("SelfDestructTime", selfDestructTimeEntry, selfdestructtimeString, "Normal"),
        ("AutoRepair", autoRepairEntry, autorepairString, "Normal"),
        ("ResupplyRange", resupplyRangeEntry, resupplyrangeString, "Normal"),
        ("MaxAutoEngageRange", maxAutoEngageRangeEntry, maxautoengagerangeString, "Normal"),
        ("FollowRadius", followRadiusEntry, followradiusString, "Normal"),
        ("OccupationRadius", occupationRadiusEntry, occupationradiusString, "Normal"),
        ("MaxElevation", maxElevationEntry, maxelevationString, "Normal"),
        ("MinElevation", minElevationEntry, minelevationString, "Normal"),
        ("ProductionPlacementRadius", productionPlacementRadiusEntry, productionplacementradiusString, "Normal"),
        ("DrawOrder", drawOrderEntry, draworderString, "Normal"),
        ("MaxNumberOnMap", maxNumberOnMapEntry, maxNumberOnMapString, "Normal"),
        ("MaxNumberOfToOrder", maxNumberToOrderEntry, maxNumberToOrderString, "Normal"),
        ("HangarSpaceRequiredEntry", hangarSpaceRequiredEntry, hangarSpaceRequiredString, "Normal"),
        ("HangarMaxLoad", hangarMaxLoadEntry, hangarMaxLoadString, "Normal")
        
    ]



    def debug():
        if hangarSpaceRequiredEntry.get() == "":
            hangarSpaceRequiredString.set("")
            print(f"HangarSpaceRequiredEntry是空的")
        else:
            hangarSpaceRequiredString.set(f"    HangarSpaceRequiredEntry 123123\n")
            print(hangarSpaceRequiredString.get())


    def checkBasicData():
        print_table()
        for i, (text, entryVar, stringVar, checkType) in enumerate(checkMap):
            if checkType == "Name":
                if globalNameEntry.get() ==  "":
                    nameString.set("")
                    print(f"{text}是空的")
                else:
                    nameString.set(f"[Unit] \"{globalNameEntry.get()}\"\n")

            elif checkType == "QuotedNormal":
                if entryVar.get() == "":
                    stringVar.set("")
                    print(f"{text}是空的")
                else:
                    stringVar.set(f"    {text} \"{entryVar.get()}\"\n")

            elif checkType == "Normal":
                if entryVar.get() == "":
                    stringVar.set("")
                    print(f"{text}是空的")
                else:
                    stringVar.set(f"    {text} {entryVar.get()}\n")

            elif checkType == "Sound":
                if soundEntry.get() == "":
                    soundString.set("")
                    print("Sound是空的")
                else:
                    # 解析输入格式：{第一个数字}, {第二个数字}
                    sound_input = soundEntry.get()
                    try:
                        # 分割字符串并提取数字
                        parts = sound_input.split(',')
                        if len(parts) == 2:
                            first_num = parts[0].strip()
                            second_num = parts[1].strip()
                            # 转换为目标格式：Sound{第一个数字} Volume{第二个数字}
                            formatted_sound = f"Sound {first_num} Volume {second_num}"
                            soundString.set(f"    {formatted_sound}\n")
                        else:
                            # 如果格式不正确，使用原始输入
                            soundString.set(f"    Sound {soundEntry.get()}\n")
                    except:
                        # 如果解析失败，使用原始输入
                        soundString.set(f"    Sound {soundEntry.get()}\n")

            else:
                print(f"[DEBUG]请新增：{checkType}类型")




    #def debug():
    #    checkBasicData()

    #调试用
    
    
    globalButtonFrame = ttk.Frame(Frame1)
    globalButtonFrame.pack(side="bottom", anchor="se", padx=10, pady=1)    
    
    ttk.Button(globalButtonFrame, command=cancelNameString, text="清除").grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(globalButtonFrame, command=fillDefault, text="默认").grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(globalButtonFrame, command=generateCode, text="生成").grid(row=0, column=3, padx=5, pady=5)
    # ttk.Button(globalButtonFrame, command=debug, text="debug").grid(row=0, column=0, padx=5, pady=5)










    screenSize = root.maxsize()
    print(screenSize)
    Width, High = screenSize


    root.geometry(f"1024x768+{int(Width*.5-512)}+{int(High*.5-384)}")
    root.resizable(False, False)

    root.mainloop()

if __name__ == "__main__":
    main()
