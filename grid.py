#全局设置
import tkinter as tk
from tkinter import ttk
from tkinter import END
from tkinter.ttk import Combobox
from tkinter import messagebox



def main():
    root = tk.Tk()
    root.title("ICBM: Escalation Unit Generator")

    # 创建主容器来更好地控制布局
    mainFrame = ttk.Frame(root)
    mainFrame.pack(fill='both', expand=True, padx=10, pady=5)

    notebook = ttk.Notebook(mainFrame)
    notebook.pack(fill='both', expand=True)

###
### 2025/10/14















    #基本信息标签页
    Frame1 = ttk.Frame(notebook)
    notebook.add(Frame1, text="基本信息和数据")
    
    # 配置Frame1的网格权重，使其能够扩展
    Frame1.columnconfigure(0, weight=1)
    Frame1.columnconfigure(1, weight=1)
    Frame1.rowconfigure(0, weight=1)
    Frame1.rowconfigure(1, weight=1)

    basicInfo = ttk.Labelframe(Frame1, text="基础数据")
    basicInfo.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")


    basicInfoFrame = ttk.Frame(basicInfo)
    basicInfoFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    basicInfoFrame.columnconfigure(0, weight=1)
    basicInfoFrame.columnconfigure(1, weight=1)





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
        ttk.Label(basicInfoFrame, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        colPropertyEntry1 = ttk.Entry(basicInfoFrame, textvariable=entryVar, width=width)
        colPropertyEntry1.grid(row=i, column=1, padx=10, pady=5, )#sticky="w")


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
            ttk.Label(basicInfoFrame, text=text).grid(row=i, column=2, padx=10, pady=5, sticky="w")
            ttk.Entry(basicInfoFrame, textvariable=entryVar, width=width).grid(row=i, column=3, padx=15, pady=5)
        if type == "type":
            ttk.Label(basicInfoFrame, text=text).grid(row=i, column=2, padx=10, pady=5, sticky="w")
            ttk.Combobox(basicInfoFrame, values=["Ground", "Airborne", "Naval", "Subwater", "Satellite"], textvariable=typeEntry, width=width).grid(row=i, column=3, padx=15, pady=5)
        if type == "crash":
            ttk.Label(basicInfoFrame, text=text).grid(row=i, column=2, padx=10, pady=5, sticky="w")
            ttk.Combobox(basicInfoFrame, values=["std_bomb", "big_bomb"], textvariable=entryVar, width=width).grid(row=i, column=3, padx=15, pady=5)



    propertyInfo = ttk.Labelframe(Frame1, text="属性数据")
    propertyInfo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

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
    customParameters.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    
    customTableData = tk.StringVar()

    def customAddToTable():
        if customEntry1.get().strip():
            customTable.insert("", tk.END, values=(customEntry1.get(), customEntry2.get()))
            customEntry1.delete(0, tk.END)
            customEntry2.delete(0, tk.END)

    def customDeleteSelected():
        if customTable.selection():
            customTable.delete(customTable.selection()[0])

    def customOutputTable():
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


    def customMapToEntries():
        selected = customTable.selection()
        if selected:
            values = customTable.item(selected[0], 'values')
            customEntry1.delete(0, tk.END)
            customEntry2.delete(0, tk.END)
            if values:
                customEntry1.insert(0, values[0])
                if len(values) > 1:
                    customEntry2.insert(0, values[1])

    def customSaveToCurrentRow():
        selected = customTable.selection()
        if not selected:
            customAddToTable()  # 无选中行则添加新行
        else:
            customTable.item(selected[0], values=(customEntry1.get(), customEntry2.get()))
            customEntry1.delete(0, tk.END)
            customEntry2.delete(0, tk.END)

    # 使用grid布局管理器来避免框架互相干扰
    customSheetFrame = ttk.Frame(customParameters)
    customSheetFrame.grid(row=0, column=0, sticky="nw", padx=5, pady=5) 

    ttk.Label(customSheetFrame, text="参数:").grid(row=0, column=0, padx=5, pady=1, sticky="w")
    customEntry1 = ttk.Entry(customSheetFrame, width=18)
    customEntry1.grid(row=1, column=0, padx=5, pady=1)
    ttk.Label(customSheetFrame, text="值").grid(row=0, column=1, padx=5, pady=1, sticky="w")
    customEntry2 = ttk.Entry(customSheetFrame, width=18)
    customEntry2.grid(row=1, column=1, padx=5, pady=1)

    customTable = ttk.Treeview(customSheetFrame, columns=("col1", "col2"), show="headings", height=12)
    customTable.heading("col1", text="参数")
    customTable.heading("col2", text="值")
    customTable.column("col1", width=140)
    customTable.column("col2", width=140)
    customTable.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    customButtonFrame = ttk.Frame(customParameters)
    customButtonFrame.grid(row=0, column=1, sticky="se", padx=1, pady=5)  

    ttk.Button(customButtonFrame, text="添加至表格", command=customAddToTable, width=12).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(customButtonFrame, text="删除选中项", command=customDeleteSelected, width=12).grid(row=1, column=0, padx=5, pady=5)

    ttk.Button(customButtonFrame, text="读取选中项", command=customMapToEntries, width=12).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(customButtonFrame, text="保存至选中项", command=customSaveToCurrentRow, width=12).grid(row=3, column=0, padx=5, pady=5)

    # ttk.Button(customButtonFrame, text="debug", command=customOutputTable, width=12).grid(row=4, column=0, padx=5, pady=5)  

    # 创建自定义参数表格的滚动条
    customScrollbar = ttk.Scrollbar(customSheetFrame, orient="vertical", command=customTable.yview)
    customTable.configure(yscrollcommand=customScrollbar.set)
    customScrollbar.grid(row=2, column=2, padx=(0, 5), pady=5, sticky="ns")
    
    # 配置网格权重使表格可以扩展
    customSheetFrame.grid_rowconfigure(2, weight=1)
    customSheetFrame.grid_columnconfigure(0, weight=1)

































    Frame2 = ttk.Frame(notebook)
    notebook.add(Frame2, text="行为控制")
    
    # 配置Frame2的网格权重，使其能够扩展
    Frame2.columnconfigure(0, weight=1)
    Frame2.rowconfigure(0, weight=1)

    behaviorCtrl = ttk.Labelframe(Frame2, text="行为控制")
    behaviorCtrl.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


    
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































    Frame3 = ttk.Frame(notebook)
    notebook.add(Frame3, text="子单位")
    
    # 配置Frame3的网格权重，使其能够扩展
    Frame3.columnconfigure(0, weight=1)
    Frame3.columnconfigure(1, weight=1)
    Frame3.columnconfigure(3, weight=1)
    Frame3.rowconfigure(0, weight=1)
    Frame3.rowconfigure(1, weight=1)


    producesFrame = ttk.Labelframe(Frame3, text="允许生产的单位")
    producesFrame.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

    producesTableData = tk.StringVar()

    def producesAddToTable():
        if producesEntry1.get().strip():
            producesTable.insert("", tk.END, values=(producesEntry1.get()))
            producesEntry1.delete(0, tk.END)

    def producesDeleteSelected():
        selected = producesTable.selection()
        if selected:
            producesTable.delete(selected[0])
    def producesOutputTable():
        items = producesTable.get_children()
        if not items:
            print("表格为空")
            producesTableData.set("")
            return ""
        table_data = ""
        for item in items:
            values = producesTable.item(item, 'values')
            if values:
                table_data += f"    Produces \"{values[0]}\"\n"
        producesTableData.set(f"\n{table_data}")
        print(producesTableData.get())
        return table_data


    def producesMapToEntries():
        selected = producesTable.selection()
        if selected:
            values = producesTable.item(selected[0], 'values')
            producesEntry1.delete(0, tk.END)
            if values:
                producesEntry1.insert(0, values[0])

    def producesSaveToCurrentRow():
        selected = producesTable.selection()
        if not selected:
            producesAddToTable()  # 无选中行则添加新行
        else:
            producesTable.item(selected[0], values=producesEntry1.get())
            producesEntry1.delete(0, tk.END)

    # 使用grid布局管理器来避免框架互相干扰
    producesSheetFrame = ttk.Frame(producesFrame)
    producesSheetFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5) 

    ttk.Label(producesSheetFrame, text="单位:").grid(row=0, column=0, padx=5, pady=1, sticky="w")
    producesEntry1 = ttk.Entry(producesSheetFrame, width=34)
    producesEntry1.grid(row=1, column=0, padx=5, pady=1)


    # 创建表格和滚动条
    producesTable = ttk.Treeview(producesSheetFrame, columns=("col1"), show="headings", height=7)
    producesTable.heading("col1", text="单位")
    producesTable.column("col1", width=240)
    
    # 创建垂直滚动条
    producesScrollbar = ttk.Scrollbar(producesSheetFrame, orient="vertical", command=producesTable.yview)
    producesTable.configure(yscrollcommand=producesScrollbar.set)
    
    # 使用grid布局放置表格和滚动条
    producesTable.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    producesScrollbar.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="ns")
    
    # 配置网格权重使表格可以扩展
    producesSheetFrame.grid_rowconfigure(2, weight=1)
    producesSheetFrame.grid_columnconfigure(0, weight=1)

    producesButtonFrame = ttk.Frame(producesFrame)
    producesButtonFrame.grid(row=3, column=0, sticky="sw", padx=5, pady=5)  
    ttk.Button(producesSheetFrame, text="+", command=producesAddToTable, width=3).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(producesSheetFrame, text="-", command=producesDeleteSelected, width=3).grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(producesButtonFrame, text="读取选中项", command=producesMapToEntries, width=10).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(producesButtonFrame, text="保存至选中项", command=producesSaveToCurrentRow, width=12).grid(row=0, column=1, padx=5, pady=5)





    canCarryUnitFrame = ttk.Labelframe(Frame3, text="允许搭载的单位")
    canCarryUnitFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    canCarryUnitTableData = tk.StringVar()

    def canCarryUnitAddToTable():
        if canCarryUnitEntry1.get().strip():
            canCarryUnitTable.insert("", tk.END, values=(canCarryUnitEntry1.get()))
            canCarryUnitEntry1.delete(0, tk.END)

    def canCarryUnitDeleteSelected():
        selected = canCarryUnitTable.selection()
        if selected:
            canCarryUnitTable.delete(selected[0])
    def canCarryUnitOutputTable():
        items = canCarryUnitTable.get_children()
        if not items:
            print("表格为空")
            canCarryUnitTableData.set("")
            return ""
        table_data = ""
        for item in items:
            values = canCarryUnitTable.item(item, 'values')
            if values:
                table_data += f"    CanCarryUnit \"{values[0]}\"\n"
        canCarryUnitTableData.set(f"\n{table_data}")
        print(canCarryUnitTableData.get())
        return table_data


    def canCarryUnitMapToEntries():
        selected = canCarryUnitTable.selection()
        if selected:
            values = canCarryUnitTable.item(selected[0], 'values')
            canCarryUnitEntry1.delete(0, tk.END)
            if values:
                canCarryUnitEntry1.insert(0, values[0])

    def canCarryUnitSaveToCurrentRow():
        selected = canCarryUnitTable.selection()
        if not selected:
            canCarryUnitAddToTable()  # 无选中行则添加新行
        else:
            canCarryUnitTable.item(selected[0], values=canCarryUnitEntry1.get())
            canCarryUnitEntry1.delete(0, tk.END)

    # 使用grid布局管理器来避免框架互相干扰
    canCarryUnitSheetFrame = ttk.Frame(canCarryUnitFrame)
    canCarryUnitSheetFrame.grid(row=0, column=0, sticky="nw", padx=5, pady=5) 

    ttk.Label(canCarryUnitSheetFrame, text="单位:").grid(row=0, column=0, padx=5, pady=1, sticky="w")
    canCarryUnitEntry1 = ttk.Entry(canCarryUnitSheetFrame, width=34)
    canCarryUnitEntry1.grid(row=1, column=0, padx=5, pady=1)


    # 创建表格和滚动条
    canCarryUnitTable = ttk.Treeview(canCarryUnitSheetFrame, columns=("col1"), show="headings", height=7)
    canCarryUnitTable.heading("col1", text="单位")
    canCarryUnitTable.column("col1", width=240)
    
    # 创建垂直滚动条
    canCarryUnitScrollbar = ttk.Scrollbar(canCarryUnitSheetFrame, orient="vertical", command=canCarryUnitTable.yview)
    canCarryUnitTable.configure(yscrollcommand=canCarryUnitScrollbar.set)
    
    # 使用grid布局放置表格和滚动条
    canCarryUnitTable.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    canCarryUnitScrollbar.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="ns")
    
    # 配置网格权重使表格可以扩展
    canCarryUnitSheetFrame.grid_rowconfigure(2, weight=1)
    canCarryUnitSheetFrame.grid_columnconfigure(0, weight=1)

    canCarryUnitButtonFrame = ttk.Frame(canCarryUnitFrame)
    canCarryUnitButtonFrame.grid(row=3, column=0, sticky="sw", padx=5, pady=5)  
    ttk.Button(canCarryUnitSheetFrame, text="+", command=canCarryUnitAddToTable, width=3).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(canCarryUnitSheetFrame, text="-", command=canCarryUnitDeleteSelected, width=3).grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(canCarryUnitButtonFrame, text="读取选中项", command=canCarryUnitMapToEntries, width=10).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(canCarryUnitButtonFrame, text="保存至选中项", command=canCarryUnitSaveToCurrentRow, width=12).grid(row=0, column=1, padx=5, pady=5)



    airwayFrame = ttk.Labelframe(Frame3, text="航线")
    airwayFrame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=5, pady=5)

    airwayTableData = tk.StringVar()  

    airwaySheetFrame = ttk.Frame(airwayFrame)
    airwaySheetFrame.grid(row=0, column=0, sticky="nw", padx=5, pady=5) 

    def airwayAddToTable():
        if airwayEntry1.get().strip() and airwayEntry2.get().strip():
            airwayTable.insert("", tk.END, values=(airwayEntry1.get(), airwayEntry2.get()))
            airwayEntry1.delete(0, tk.END)
            airwayEntry2.delete(0, tk.END)

    def airwayDeleteSelected():
        selected = airwayTable.selection()
        if selected:
            airwayTable.delete(selected[0])


    def airwayOutputTable():
        items = airwayTable.get_children()
        if len(items) < 1:
            print("airwayTable内的行数小于1")
        if not items:
            print("表格为空")
            airwayTableData.set("")
            return ""
        table_data = ""
        for item in items:
            values = airwayTable.item(item, 'values')
            if values:
                table_data += f"    Airway Launch {values[0]} Time {values[1]}\n"
        airwayTableData.set(f"\n{table_data}")
        print(airwayTableData.get())

    def airwayConfig():
        print("airwayIsConfigNow")

    def airwayMapToEntries():
        selected = airwayTable.selection()
        if selected:
            values = airwayTable.item(selected[0], 'values')
            airwayEntry1.delete(0, tk.END)
            airwayEntry2.delete(0, tk.END)
            if values:
                airwayEntry1.insert(0, values[0])
                if len(values) > 1:
                    airwayEntry2.insert(0, values[1])

    def airwaySaveToCurrentRow():
        selected = airwayTable.selection()
        if not selected:
            airwayAddToTable()  # 无选中行则添加新行
        else:
            airwayTable.item(selected[0], values=(airwayEntry1.get(), airwayEntry2.get()))
            airwayEntry1.delete(0, tk.END)
            airwayEntry2.delete(0, tk.END)

    airwayTable = ttk.Treeview(airwaySheetFrame, columns=("col1", "col2"), show="headings", height=24)
    airwayTable.heading("col1", text="单次发射数")
    airwayTable.heading("col2", text="时间间隔")
    airwayTable.column("col1", width=90)
    airwayTable.column("col2", width=90)
    airwayTable.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    airwaySheetFrame.grid_rowconfigure(2, weight=1)
    airwaySheetFrame.grid_columnconfigure(0, weight=1)
    airwayButtonFrame = ttk.Frame(airwayFrame)
    airwayButtonFrame.grid(row=3, column=0, sticky="ws", padx=5, pady=5)  

    ttk.Label(airwaySheetFrame, text="单次发射:").grid(row=0, column=0, padx=5, pady=1, sticky="w")
    ttk.Label(airwaySheetFrame, text="发射间隔:").grid(row=1, column=0, padx=5, pady=1, sticky="w")
    airwayEntry1 = ttk.Entry(airwaySheetFrame, width=16)
    airwayEntry1.grid(row=0, column=1, padx=5, pady=1)
    airwayEntry2 = ttk.Entry(airwaySheetFrame, width=16)
    airwayEntry2.grid(row=1, column=1, padx=5, pady=1)
    ttk.Button(airwaySheetFrame, text="+", command=airwayAddToTable, width=3).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(airwaySheetFrame, text="-", command=airwayDeleteSelected, width=3).grid(row=1, column=2, padx=5, pady=5)
    ttk.Button(airwayButtonFrame, text="读取选中项", command=airwayMapToEntries, width=10).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(airwayButtonFrame, text="保存选中项", command=airwaySaveToCurrentRow, width=12).grid(row=0, column=1, padx=5, pady=5)    

    airwayScrollbar = ttk.Scrollbar(airwaySheetFrame, orient="vertical", command=airwayTable.yview)
    airwayTable.configure(yscrollcommand=airwayScrollbar.set)
    airwayScrollbar.grid(row=2, column=2, padx=(0, 5), pady=5, sticky="ns")
    


    canHostAircraftsFrame = ttk.Labelframe(Frame3, text="子单位")
    canHostAircraftsFrame.grid(row=0, column=3, rowspan=2, sticky="nsew", padx=5, pady=5)

    canHostAircraftsEntryFrame = ttk.Frame(canHostAircraftsFrame)
    canHostAircraftsEntryFrame.grid(row=0, column=0, sticky="nw", padx=5, pady=5) 

    canHostAircraftsSheetFrame = ttk.Frame(canHostAircraftsFrame)
    canHostAircraftsSheetFrame.grid(row=1, column=0, sticky="w", padx=5, pady=5) 

    canHostAircraftsTableData = tk.StringVar()  
    canHostAircraftsCheckboxVar = tk.BooleanVar()

    def canHostAircraftsAddToTable():
        if canHostAircraftsEntry1.get().strip():
            canHostAircraftsTable.insert("", tk.END, values=(
                canHostAircraftsEntry1.get(),
                canHostAircraftsEntry2.get(),
                canHostAircraftsEntry3.get(),
                canHostAircraftsEntry4.get(),
                "√" if canHostAircraftsCheckboxVar.get() else ""
            ))
            canHostAircraftsEntry1.delete(0, tk.END)
            canHostAircraftsEntry2.delete(0, tk.END)
            canHostAircraftsEntry3.delete(0, tk.END)
            canHostAircraftsEntry4.delete(0, tk.END)
            canHostAircraftsCheckboxVar.set(False)

    def canHostAircraftsDeleteSelected():
        selected = canHostAircraftsTable.selection()
        if selected:
            canHostAircraftsTable.delete(selected[0])

    def canHostAircraftsMapToEntries():
        selected = canHostAircraftsTable.selection()
        if selected:
            values = canHostAircraftsTable.item(selected[0], 'values')
            canHostAircraftsEntry1.delete(0, tk.END)
            canHostAircraftsEntry2.delete(0, tk.END)
            canHostAircraftsEntry3.delete(0, tk.END)
            canHostAircraftsEntry4.delete(0, tk.END)
            if values:
                canHostAircraftsEntry1.insert(0, values[0])
                if len(values) > 1:
                    canHostAircraftsEntry2.insert(0, values[1])
                if len(values) > 2:
                    canHostAircraftsEntry3.insert(0, values[2])
                if len(values) > 3:
                    canHostAircraftsEntry4.insert(0, values[3])
                if len(values) > 4:
                    canHostAircraftsCheckboxVar.set(values[4] == "√")
                else:
                    canHostAircraftsCheckboxVar.set(False)

    def canHostAircraftsSaveToCurrentRow():
        selected = canHostAircraftsTable.selection()
        if not selected:
            canHostAircraftsAddToTable()  # 无选中行则添加新行
        else:
            canHostAircraftsTable.item(selected[0], values=(
                canHostAircraftsEntry1.get(),
                canHostAircraftsEntry2.get(),
                canHostAircraftsEntry3.get(),
                canHostAircraftsEntry4.get(),
                "√" if canHostAircraftsCheckboxVar.get() else ""
            ))
            canHostAircraftsEntry1.delete(0, tk.END)
            canHostAircraftsEntry2.delete(0, tk.END)
            canHostAircraftsEntry3.delete(0, tk.END)
            canHostAircraftsEntry4.delete(0, tk.END)
            canHostAircraftsCheckboxVar.set(False)

    def canHostAircraftsOutputTable():
        items = canHostAircraftsTable.get_children()
        if not items:
            print("表格为空")
            canHostAircraftsTableData.set("")
            return ""
        table_data = ""
        for item in items:
            values = canHostAircraftsTable.item(item, 'values')
            if values:
                # 安全地获取各个字段的值，避免索引越界
                unit_name = values[0] if len(values) > 0 else ""
                unit_count = values[1] if len(values) > 1 else ""
                airway = values[2] if len(values) > 2 else ""
                patrol_count = values[3] if len(values) > 3 else ""
                auto_patrol = values[4] if len(values) > 4 else ""
                
                # 检查航线（airway）和巡逻数（patrol_count）是否为空
                has_airway = airway and airway.strip()
                has_patrol = patrol_count and patrol_count.strip()
                has_auto_patrol = auto_patrol == "√"
                
                if has_airway and has_patrol:
                    # 既有航线又有巡逻数
                    if has_auto_patrol:
                        table_data += f"    CanHostAircrafts airway {airway} \"{unit_name}\" {unit_count} Patrol {patrol_count} AIAutoPatrol\n"
                    else:
                        table_data += f"    CanHostAircrafts airway {airway} \"{unit_name}\" {unit_count} Patrol {patrol_count}\n"
                elif has_airway and not has_patrol:
                    # 只有航线，没有巡逻数
                    table_data += f"    CanHostAircrafts airway {airway} \"{unit_name}\" {unit_count}\n"
                elif not has_airway and has_patrol:
                    # 只有巡逻数，没有航线
                    if has_auto_patrol:
                        table_data += f"    CanHostAircrafts \"{unit_name}\" {unit_count} Patrol {patrol_count} AIAutoPatrol\n"
                    else:
                        table_data += f"    CanHostAircrafts \"{unit_name}\" {unit_count} Patrol {patrol_count}\n"
                else:
                    # 既没有航线也没有巡逻数
                    table_data += f"    CanHostAircrafts \"{unit_name}\" {unit_count}\n"
        canHostAircraftsTableData.set(table_data)
        print(canHostAircraftsTableData.get())
        return table_data        

    canHostAircraftsButtonFrame = ttk.Frame(canHostAircraftsFrame)
    canHostAircraftsButtonFrame.grid(row=2, column=0, sticky="w", padx=5, pady=5)  

    canHostAircraftsTable = ttk.Treeview(canHostAircraftsSheetFrame, columns=("col1", "col2", "col3", "col4", "col5"), show="headings", height=24)
    canHostAircraftsTable.heading("col1", text="单位")
    canHostAircraftsTable.heading("col2", text="数量")
    canHostAircraftsTable.heading("col3", text="航线")
    canHostAircraftsTable.heading("col4", text="巡逻数")
    canHostAircraftsTable.heading("col5", text="自巡逻")
    canHostAircraftsTable.column("col1", width=150)
    canHostAircraftsTable.column("col2", width=50)
    canHostAircraftsTable.column("col3", width=50)
    canHostAircraftsTable.column("col4", width=50)
    canHostAircraftsTable.column("col5", width=50)
    canHostAircraftsTable.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    ttk.Label(canHostAircraftsEntryFrame, text="单位名称:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(canHostAircraftsEntryFrame, text="单位数量:").grid(row=0, column=5, padx=5, pady=5, sticky="w")
    ttk.Label(canHostAircraftsEntryFrame, text="航线选择:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
    ttk.Label(canHostAircraftsEntryFrame, text="巡逻数量:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    ttk.Label(canHostAircraftsEntryFrame, text="自动巡逻").grid(row=1, column=6, padx=5, pady=5, sticky="w")
    
    canHostAircraftsEntry1 = ttk.Entry(canHostAircraftsEntryFrame, width=24)
    canHostAircraftsEntry1.grid(row=0, column=1, padx=5, pady=5, columnspan=3)
    canHostAircraftsEntry2 = ttk.Entry(canHostAircraftsEntryFrame, width=6)
    canHostAircraftsEntry2.grid(row=0, column=6, padx=5, pady=5)
    canHostAircraftsEntry3 = ttk.Entry(canHostAircraftsEntryFrame, width=6)
    canHostAircraftsEntry3.grid(row=1, column=3, padx=5, pady=5)
    canHostAircraftsEntry4 = ttk.Entry(canHostAircraftsEntryFrame, width=6)
    canHostAircraftsEntry4.grid(row=1, column=1, padx=5, pady=5)

    ttk.Checkbutton(canHostAircraftsEntryFrame, variable=canHostAircraftsCheckboxVar).grid(row=1, column=5, padx=5, pady=5)

    ttk.Button(canHostAircraftsButtonFrame, text="+", command=canHostAircraftsAddToTable, width=3).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(canHostAircraftsButtonFrame, text="-", command=canHostAircraftsDeleteSelected, width=3).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(canHostAircraftsButtonFrame, text="读取选中项", command=canHostAircraftsMapToEntries, width=12).grid(row=0, column=2, padx=5, pady=5)
    ttk.Button(canHostAircraftsButtonFrame, text="保存至选中项", command=canHostAircraftsSaveToCurrentRow, width=12).grid(row=0, column=3, padx=5, pady=5)    

    canHostAircraftsScrollbar = ttk.Scrollbar(canHostAircraftsSheetFrame, orient="vertical", command=canHostAircraftsTable.yview)
    canHostAircraftsTable.configure(yscrollcommand=canHostAircraftsScrollbar.set)
    canHostAircraftsScrollbar.grid(row=0, column=2, padx=(0, 5), pady=5, sticky="ns")


















    Frame4 = ttk.Frame(notebook)
    notebook.add(Frame4, text="武器和雷达")

    # 配置Frame4的网格权重，使其能够扩展
    Frame4.columnconfigure(0, weight=1)
    Frame4.rowconfigure(0, weight=1)

    missileFrame = ttk.Labelframe(Frame4, text="导弹配置")
    missileFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # 导弹配置数据管理器
    class MissileConfigManager:
        """导弹配置数据管理器"""
        
        def __init__(self):
            self.config_data_dict = {}
            self.weapon_data_dict = {}
            self.initialize_default_config()
        
        def initialize_default_config(self):
            """初始化默认配置"""
            default_id = "default_config"
            self.config_data_dict[default_id] = {
                'name': '默认', 
                'only_full': False, 
                'default': True, 
                'improved_by': [], 
                'weapons': []
            }
        
        def add_config(self, name, only_full=False, default=False):
            """添加新配置"""
            if not name or name == "默认":
                return False
            
            config_id = f"config_{len(self.config_data_dict)}"
            self.config_data_dict[config_id] = {
                'name': name, 
                'only_full': only_full, 
                'default': default, 
                'improved_by': [], 
                'weapons': []
            }
            return config_id
        
        def add_improved_by(self, parent_config_name, improved_name):
            """添加升级项"""
            parent_id = self._find_config_id_by_name(parent_config_name)
            if not parent_id:
                return False
            
            self.config_data_dict[parent_id]['improved_by'].append({
                'name': improved_name, 
                'weapons': []
            })
            
            # 为升级项创建武器数据存储
            improved_config_id = f"improved_{parent_id}_{improved_name}"
            if improved_config_id not in self.weapon_data_dict:
                self.weapon_data_dict[improved_config_id] = []
            
            # 计算这是父配置的第几个升级项，用于生成武器名称
            parent_config = self.config_data_dict[parent_id]
            improved_index = len(parent_config['improved_by'])
            
            # 自动为升级项添加一个默认武器（使用weapon1, weapon2, weapon3等名称）
            default_weapon = {
                'name': f'weapon{improved_index}', 
                'ammo': str(improved_index), 
                'launch_count': '', 
                'launch_time': '',
                'auto_engage': False, 
                'principal': False, 
                'default_off': False
            }
            self.weapon_data_dict[improved_config_id].append(default_weapon)
            
            return True
        
        def add_weapon(self, config_id, weapon_data):
            """添加武器到配置"""
            if config_id not in self.weapon_data_dict:
                self.weapon_data_dict[config_id] = []
            
            self.weapon_data_dict[config_id].append(weapon_data)
            return len(self.weapon_data_dict[config_id])
        
        def update_weapon(self, config_id, weapon_index, weapon_data):
            """更新武器数据"""
            if (config_id in self.weapon_data_dict and 
                weapon_index < len(self.weapon_data_dict[config_id])):
                self.weapon_data_dict[config_id][weapon_index] = weapon_data
                return True
            return False
        
        def delete_weapon(self, config_id, weapon_index):
            """删除武器"""
            if (config_id in self.weapon_data_dict and 
                weapon_index < len(self.weapon_data_dict[config_id])):
                self.weapon_data_dict[config_id].pop(weapon_index)
                return True
            return False
        
        def get_weapons(self, config_id):
            """获取配置的武器列表"""
            return self.weapon_data_dict.get(config_id, [])
        
        def get_configs(self):
            """获取所有配置"""
            return self.config_data_dict
        
        def _find_config_id_by_name(self, name):
            """根据名称查找配置ID"""
            for config_id, config in self.config_data_dict.items():
                if config['name'] == name:
                    return config_id
            return None

    # 配置面板组件
    class ConfigPanel:
        """配置面板组件"""
        
        def __init__(self, parent_frame, config_manager, on_config_select_callback):
            self.parent_frame = parent_frame
            self.config_manager = config_manager
            self.on_config_select_callback = on_config_select_callback
            self.selected_config_id = None
            
            self.create_ui_components()
            self.refresh_config_list()
        
        def create_ui_components(self):
            """创建UI组件"""
            # 配置框架
            config_frame = ttk.Labelframe(self.parent_frame, text="配置列表")
            config_frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            # 输入区域
            config_input_frame = ttk.Frame(config_frame)
            config_input_frame.pack(fill='x', padx=5, pady=5)
            
            # 第一行：名称输入框和上移按钮
            row1_frame = ttk.Frame(config_input_frame)
            row1_frame.pack(fill='x', pady=(0, 5))
            ttk.Label(row1_frame, text="名称:").pack(side='left', padx=(0, 5))
            self.config_name_entry = ttk.Entry(row1_frame, width=20)
            self.config_name_entry.pack(side='left', padx=(0, 10))
            ttk.Button(row1_frame, text="↑", command=self.move_up_config, width=3).pack(side='right', padx=(5, 0))
            
            # 第二行：复选框和下移按钮
            row2_frame = ttk.Frame(config_input_frame)
            row2_frame.pack(fill='x')
            self.config_only_full_var = tk.BooleanVar()
            self.config_default_var = tk.BooleanVar()
            ttk.Checkbutton(row2_frame, text="OnlyFull", variable=self.config_only_full_var).pack(side='left', padx=(0, 10))
            ttk.Checkbutton(row2_frame, text="Default", variable=self.config_default_var).pack(side='left', padx=(0, 10))
            ttk.Button(row2_frame, text="↓", command=self.move_down_config, width=3).pack(side='right', padx=(5, 0))
            
            # 配置树形视图
            config_tree_frame = ttk.Frame(config_frame)
            config_tree_frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            columns = ('weapon_count', 'only_full', 'default')
            self.config_tree = ttk.Treeview(config_tree_frame, columns=columns, show='tree headings', height=12)
            self.config_tree.heading('#0', text='名称')
            self.config_tree.column('#0', width=180)
            self.config_tree.heading('weapon_count', text='武器数量')
            self.config_tree.column('weapon_count', width=70)
            self.config_tree.heading('only_full', text='OnlyFull')
            self.config_tree.column('only_full', width=60)
            self.config_tree.heading('default', text='Default')
            self.config_tree.column('default', width=60)
            
            config_scrollbar = ttk.Scrollbar(config_tree_frame, orient='vertical', command=self.config_tree.yview)
            self.config_tree.configure(yscrollcommand=config_scrollbar.set)
            self.config_tree.pack(side='left', fill='both', expand=True)
            config_scrollbar.pack(side='right', fill='y')
            self.config_tree.bind('<<TreeviewSelect>>', self.on_config_select)
            
            # 按钮区域
            config_button_frame = ttk.Frame(config_frame)
            config_button_frame.pack(fill='x', padx=5, pady=5)
            ttk.Button(config_button_frame, text="添加配置", command=self.add_config, width=8).pack(side='left', padx=(0, 5))
            ttk.Button(config_button_frame, text="添加升级项", command=self.add_improved_by, width=10).pack(side='left', padx=(0, 5))
            ttk.Button(config_button_frame, text="-", command=self.delete_selected, width=3).pack(side='left', padx=(0, 5))
            ttk.Button(config_button_frame, text="读取选中项", command=self.load_selected_config, width=10).pack(side='left', padx=(0, 5))
            ttk.Button(config_button_frame, text="保存至选中项", command=self.save_to_selected_config, width=12).pack(side='left', padx=(0, 5))
        
        def refresh_config_list(self):
            """刷新配置列表"""
            for item in self.config_tree.get_children():
                self.config_tree.delete(item)
            
            configs = self.config_manager.get_configs()
            for config_id, config in configs.items():
                # 计算配置的武器数量（包括自身的武器）
                weapon_count = len(self.config_manager.get_weapons(config_id))
                only_full_text = "是" if config['only_full'] else "否"
                default_text = "是" if config['default'] else "否"
                
                item_id = self.config_tree.insert('', 'end', text=config['name'], 
                                                values=(str(weapon_count), only_full_text, default_text))
                
                # 添加升级项
                for improved in config['improved_by']:
                    # 计算升级项的武器数量
                    improved_config_id = f"improved_{config_id}_{improved['name']}"
                    improved_weapon_count = len(self.config_manager.get_weapons(improved_config_id))
                    self.config_tree.insert(item_id, 'end', text=improved['name'], 
                                          values=(str(improved_weapon_count), '否', '否'))
        
        def add_config(self):
            """添加配置"""
            name = self.config_name_entry.get().strip()
            if not name:
                messagebox.showwarning("错误", "请检查字段是否填写完整")
                return
            
            if name == "默认":
                messagebox.showwarning("错误", "不支持的键入")
                return
            
            config_id = self.config_manager.add_config(
                name, 
                self.config_only_full_var.get(), 
                self.config_default_var.get()
            )
            
            if config_id:
                only_full_text = "是" if self.config_only_full_var.get() else "否"
                default_text = "是" if self.config_default_var.get() else "否"
                self.config_tree.insert('', 'end', text=name, values=('0', only_full_text, default_text))
                self.clear_config_inputs()
        
        def add_improved_by(self):
            """添加升级项"""
            if not self.selected_config_id:
                messagebox.showwarning("错误", "请先选择一个配置")
                return
            
            name = self.config_name_entry.get().strip()
            if not name:
                messagebox.showwarning("错误", "请检查字段是否填写完整")
                return
            
            config_name = self.config_tree.item(self.selected_config_id)['text']
            if self.config_manager.add_improved_by(config_name, name):
                only_full_text = "是" if self.config_only_full_var.get() else "否"
                default_text = "是" if self.config_default_var.get() else "否"
                self.config_tree.insert(self.selected_config_id, 'end', text=name, 
                                      values=('0', only_full_text, default_text))
                self.config_tree.item(self.selected_config_id, open=True)
                self.clear_config_inputs()
        
        def on_config_select(self, event):
            """配置选择事件"""
            selection = self.config_tree.selection()
            if selection:
                self.selected_config_id = selection[0]
                if self.on_config_select_callback:
                    self.on_config_select_callback(self.selected_config_id)
        
        def load_selected_config(self):
            """读取选中配置"""
            if not self.selected_config_id:
                return
            
            item_text = self.config_tree.item(self.selected_config_id)['text']
            values = self.config_tree.item(self.selected_config_id)['values']
            
            if item_text == '默认':
                messagebox.showwarning("限制", "不允许修改")
                return
            
            self.config_name_entry.delete(0, tk.END)
            self.config_name_entry.insert(0, item_text)
            
            if values:
                self.config_only_full_var.set(values[1] == '是')
                self.config_default_var.set(values[2] == '是')
        
        def save_to_selected_config(self):
            """保存到选中配置"""
            if not self.selected_config_id:
                return
            
            item_text = self.config_tree.item(self.selected_config_id)['text']
            if item_text == '默认':
                messagebox.showwarning("限制", "不允许修改")
                return
            
            name = self.config_name_entry.get().strip()
            if not name:
                messagebox.showwarning("错误", "请检查字段是否填写完整")
                return
            
            only_full_text = "是" if self.config_only_full_var.get() else "否"
            default_text = "是" if self.config_default_var.get() else "否"
            weapon_count = self.config_tree.item(self.selected_config_id)['values'][0]
            
            self.config_tree.item(self.selected_config_id, text=name, 
                                values=(weapon_count, only_full_text, default_text))
            self.clear_config_inputs()
        
        def move_up_config(self):
            """上移配置"""
            if not self.selected_config_id:
                messagebox.showwarning("错误", "请先选择一个项")
                return
            
            item_text = self.config_tree.item(self.selected_config_id)['text']
            if item_text == '默认':
                messagebox.showwarning("限制", "不允许移动")
                return
            
            parent = self.config_tree.parent(self.selected_config_id)
            if parent:
                # ImprovedBy子项移动逻辑
                all_siblings = list(self.config_tree.get_children(parent))
                current_index = all_siblings.index(self.selected_config_id)
                
                if current_index <= 0:
                    messagebox.showwarning("限制", "已是第一个")
                    return
                
                self.config_tree.move(self.selected_config_id, parent, current_index - 1)
            else:
                # 顶级Config项移动逻辑
                all_items = list(self.config_tree.get_children())
                current_index = all_items.index(self.selected_config_id)
                
                if current_index <= 1:  # 索引0是默认配置，索引1是第一个可移动项
                    messagebox.showwarning("限制", "已是第一个")
                    return
                
                self.config_tree.move(self.selected_config_id, '', current_index - 1)
            
            self.config_tree.selection_set(self.selected_config_id)
        
        def move_down_config(self):
            """下移配置"""
            if not self.selected_config_id:
                messagebox.showwarning("错误", "请先选择一个项")
                return
            
            item_text = self.config_tree.item(self.selected_config_id)['text']
            if item_text == '默认':
                messagebox.showwarning("限制", "不允许移动")
                return
            
            parent = self.config_tree.parent(self.selected_config_id)
            if parent:
                # ImprovedBy子项移动逻辑
                all_siblings = list(self.config_tree.get_children(parent))
                current_index = all_siblings.index(self.selected_config_id)
                
                if current_index >= len(all_siblings) - 1:
                    messagebox.showwarning("限制", "已是最后一个")
                    return
                
                self.config_tree.move(self.selected_config_id, parent, current_index + 1)
            else:
                # 顶级Config项移动逻辑
                all_items = list(self.config_tree.get_children())
                current_index = all_items.index(self.selected_config_id)
                
                if current_index >= len(all_items) - 1:
                    messagebox.showwarning("限制", "已是最后一项")
                    return
                
                self.config_tree.move(self.selected_config_id, '', current_index + 1)
            
            self.config_tree.selection_set(self.selected_config_id)
        
        def delete_selected(self):
            """删除选中行"""
            if not self.selected_config_id:
                messagebox.showwarning("错误", "请先选择一个项")
                return
            
            item_text = self.config_tree.item(self.selected_config_id)['text']
            
            # 不允许删除默认配置
            if item_text == '默认':
                messagebox.showwarning("限制", "不允许删除默认配置")
                return
            
            # 判断是Config还是ImprovedBy
            parent = self.config_tree.parent(self.selected_config_id)
            if parent:
                # 删除ImprovedBy
                parent_text = self.config_tree.item(parent)['text']
                parent_id = self.config_manager._find_config_id_by_name(parent_text)
                if parent_id:
                    # 从父配置的improved_by列表中删除
                    config = self.config_manager.config_data_dict[parent_id]
                    config['improved_by'] = [improved for improved in config['improved_by'] if improved['name'] != item_text]
                    
                    # 删除对应的武器数据
                    improved_config_id = f"improved_{parent_id}_{item_text}"
                    if improved_config_id in self.config_manager.weapon_data_dict:
                        del self.config_manager.weapon_data_dict[improved_config_id]
            else:
                # 删除Config
                config_id = self.config_manager._find_config_id_by_name(item_text)
                if config_id:
                    # 删除配置数据
                    del self.config_manager.config_data_dict[config_id]
                    
                    # 删除对应的武器数据
                    if config_id in self.config_manager.weapon_data_dict:
                        del self.config_manager.weapon_data_dict[config_id]
                    
                    # 删除所有相关的ImprovedBy武器数据
                    for key in list(self.config_manager.weapon_data_dict.keys()):
                        if key.startswith(f"improved_{config_id}_"):
                            del self.config_manager.weapon_data_dict[key]
            
            # 刷新配置列表
            self.refresh_config_list()
            self.clear_config_inputs()
            self.selected_config_id = None
        
        def clear_config_inputs(self):
            """清空配置输入"""
            self.config_name_entry.delete(0, tk.END)
            self.config_only_full_var.set(False)
            self.config_default_var.set(False)

    # 武器面板组件
    class WeaponPanel:
        """武器面板组件"""
        
        def __init__(self, parent_frame, config_manager, on_weapon_update_callback):
            self.parent_frame = parent_frame
            self.config_manager = config_manager
            self.on_weapon_update_callback = on_weapon_update_callback
            self.selected_config_id = None
            
            self.create_ui_components()
        
        def create_ui_components(self):
            """创建UI组件"""
            # 武器框架
            weapon_frame = ttk.Labelframe(self.parent_frame, text="武器列表")
            weapon_frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            # 输入区域
            weapon_input_frame = ttk.Frame(weapon_frame)
            weapon_input_frame.pack(fill='x', padx=5, pady=5)
            
            # 第一行：武器名称和复选框
            row1_frame = ttk.Frame(weapon_input_frame)
            row1_frame.pack(fill='x', pady=(0, 5))
            ttk.Label(row1_frame, text="武器名称:").grid(row=0, column=0, padx=(0, 5), sticky='w')
            self.weapon_name_entry = ttk.Entry(row1_frame, width=20)
            self.weapon_name_entry.grid(row=0, column=1, padx=(0, 10))
            
            self.weapon_auto_engage_var = tk.BooleanVar()
            self.weapon_principal_var = tk.BooleanVar()
            self.weapon_default_off_var = tk.BooleanVar()
            ttk.Checkbutton(row1_frame, text="自动接敌", variable=self.weapon_auto_engage_var).grid(row=0, column=2, padx=(0, 10))
            ttk.Checkbutton(row1_frame, text="显示备弹", variable=self.weapon_principal_var).grid(row=0, column=3, padx=(0, 10))
            ttk.Checkbutton(row1_frame, text="默认关闭", variable=self.weapon_default_off_var).grid(row=0, column=4)
            
            # 第二行：武器参数
            row2_frame = ttk.Frame(weapon_input_frame)
            row2_frame.pack(fill='x')
            ttk.Label(row2_frame, text="备弹数量:").grid(row=0, column=0, padx=(0, 5), sticky='w')
            self.weapon_ammo_entry = ttk.Entry(row2_frame, width=8)
            self.weapon_ammo_entry.grid(row=0, column=1, padx=(0, 10))
            ttk.Label(row2_frame, text="发射数量:").grid(row=0, column=2, padx=(0, 5), sticky='w')
            self.weapon_launch_count_entry = ttk.Entry(row2_frame, width=8)
            self.weapon_launch_count_entry.grid(row=0, column=3, padx=(0, 10))
            ttk.Label(row2_frame, text="发射时间:").grid(row=0, column=4, padx=(0, 5), sticky='w')
            self.weapon_launch_time_entry = ttk.Entry(row2_frame, width=8)
            self.weapon_launch_time_entry.grid(row=0, column=5, padx=(0, 10))
            
            # 武器表格
            weapon_tree_frame = ttk.Frame(weapon_frame)
            weapon_tree_frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            columns = ('name', 'ammo', 'launch_count', 'launch_time', 'auto_engage', 'principal', 'default_off')
            self.weapon_tree = ttk.Treeview(weapon_tree_frame, columns=columns, show='headings', height=12)
            self.weapon_tree.heading('name', text='武器名称')
            self.weapon_tree.column('name', width=120)
            self.weapon_tree.heading('ammo', text='备弹数量')
            self.weapon_tree.column('ammo', width=50)
            self.weapon_tree.heading('launch_count', text='发射数量')
            self.weapon_tree.column('launch_count', width=50)
            self.weapon_tree.heading('launch_time', text='发射时间')
            self.weapon_tree.column('launch_time', width=50)
            self.weapon_tree.heading('auto_engage', text='自动接敌')
            self.weapon_tree.column('auto_engage', width=50)
            self.weapon_tree.heading('principal', text='显示备弹')
            self.weapon_tree.column('principal', width=50)
            self.weapon_tree.heading('default_off', text='默认关闭')
            self.weapon_tree.column('default_off', width=50)
            
            weapon_scrollbar = ttk.Scrollbar(weapon_tree_frame, orient='vertical', command=self.weapon_tree.yview)
            self.weapon_tree.configure(yscrollcommand=weapon_scrollbar.set)
            self.weapon_tree.pack(side='left', fill='both', expand=True)
            weapon_scrollbar.pack(side='right', fill='y')
            
            # 按钮区域
            weapon_ops_frame = ttk.Frame(weapon_frame)
            weapon_ops_frame.pack(fill='x', padx=5, pady=5)
            ttk.Button(weapon_ops_frame, text="+", command=self.add_weapon, width=3).pack(side='left', padx=(0, 5))
            ttk.Button(weapon_ops_frame, text="-", command=self.delete_selected_weapon, width=3).pack(side='left', padx=(0, 5))
            ttk.Button(weapon_ops_frame, text="读取", command=self.load_selected_weapon, width=8).pack(side='left', padx=(0, 5))
            ttk.Button(weapon_ops_frame, text="保存", command=self.save_to_selected_weapon, width=8).pack(side='left', padx=(0, 5))
            
        
        def set_selected_config(self, config_id):
            """设置选中的配置"""
            self.selected_config_id = config_id
            self.refresh_weapon_list()
        
        def get_selected_config_id(self):
            """获取选中的配置ID"""
            return self.selected_config_id
        
        def refresh_weapon_list(self):
            """刷新武器列表"""
            for item in self.weapon_tree.get_children():
                self.weapon_tree.delete(item)
            
            if self.selected_config_id:
                weapons = self.config_manager.get_weapons(self.selected_config_id)
                for weapon in weapons:
                    auto_engage_text = "是" if weapon['auto_engage'] else "否"
                    principal_text = "是" if weapon['principal'] else "否"
                    default_off_text = "是" if weapon['default_off'] else "否"
                    self.weapon_tree.insert('', 'end', values=(
                        weapon['name'], weapon['ammo'], weapon['launch_count'], weapon['launch_time'],
                        auto_engage_text, principal_text, default_off_text
                    ))
        
        def add_weapon(self):
            """添加武器"""
            if not self.selected_config_id:
                messagebox.showwarning("错误", "请先选择一个配置或升级项")
                return
            
            name = self.weapon_name_entry.get().strip()
            ammo = self.weapon_ammo_entry.get().strip()
            launch_count = self.weapon_launch_count_entry.get().strip()
            launch_time = self.weapon_launch_time_entry.get().strip()
            
            if not name or not ammo:
                messagebox.showwarning("错误", "请检查字段是否填写完整")
                return
            
            weapon_data = {
                'name': name, 
                'ammo': ammo, 
                'launch_count': launch_count, 
                'launch_time': launch_time, 
                'auto_engage': self.weapon_auto_engage_var.get(), 
                'principal': self.weapon_principal_var.get(), 
                'default_off': self.weapon_default_off_var.get()
            }
            
            weapon_count = self.config_manager.add_weapon(self.selected_config_id, weapon_data)
            
            auto_engage_text = "是" if self.weapon_auto_engage_var.get() else "否"
            principal_text = "是" if self.weapon_principal_var.get() else "否"
            default_off_text = "是" if self.weapon_default_off_var.get() else "否"
            
            self.weapon_tree.insert('', 'end', values=(
                name, ammo, launch_count, launch_time, auto_engage_text, principal_text, default_off_text
            ))
            
            if self.on_weapon_update_callback:
                self.on_weapon_update_callback(self.selected_config_id, weapon_count)
            
            self.clear_weapon_inputs()
        
        def delete_selected_weapon(self):
            """删除选中武器"""
            selection = self.weapon_tree.selection()
            if not selection:
                return
            
            if not messagebox.askyesno("删除", "确定要删除选中的武器吗？"):
                return
            
            selected_index = self.weapon_tree.index(selection[0])
            if self.config_manager.delete_weapon(self.selected_config_id, selected_index):
                weapon_count = len(self.config_manager.get_weapons(self.selected_config_id))
                self.weapon_tree.delete(selection[0])
                
                if self.on_weapon_update_callback:
                    self.on_weapon_update_callback(self.selected_config_id, weapon_count)
        
        def load_selected_weapon(self):
            """读取选中武器"""
            selection = self.weapon_tree.selection()
            if not selection:
                return
            
            values = self.weapon_tree.item(selection[0])['values']
            if values:
                self.weapon_name_entry.delete(0, tk.END)
                self.weapon_name_entry.insert(0, values[0])
                self.weapon_ammo_entry.delete(0, tk.END)
                self.weapon_ammo_entry.insert(0, values[1])
                self.weapon_launch_count_entry.delete(0, tk.END)
                self.weapon_launch_count_entry.insert(0, values[2])
                self.weapon_launch_time_entry.delete(0, tk.END)
                self.weapon_launch_time_entry.insert(0, values[3])
                self.weapon_auto_engage_var.set(values[4] == '是')
                self.weapon_principal_var.set(values[5] == '是')
                self.weapon_default_off_var.set(values[6] == '是')
        
        def save_to_selected_weapon(self):
            """保存到选中武器"""
            selection = self.weapon_tree.selection()
            if not selection:
                return
            
            name = self.weapon_name_entry.get().strip()
            ammo = self.weapon_ammo_entry.get().strip()
            launch_count = self.weapon_launch_count_entry.get().strip()
            launch_time = self.weapon_launch_time_entry.get().strip()
            
            if not name or not ammo:
                messagebox.showwarning("错误", "请检查字段是否填写完整")
                return
            
            weapon_data = {
                'name': name, 
                'ammo': ammo, 
                'launch_count': launch_count, 
                'launch_time': launch_time, 
                'auto_engage': self.weapon_auto_engage_var.get(), 
                'principal': self.weapon_principal_var.get(), 
                'default_off': self.weapon_default_off_var.get()
            }
            
            selected_index = self.weapon_tree.index(selection[0])
            if self.config_manager.update_weapon(self.selected_config_id, selected_index, weapon_data):
                auto_engage_text = "是" if self.weapon_auto_engage_var.get() else "否"
                principal_text = "是" if self.weapon_principal_var.get() else "否"
                default_off_text = "是" if self.weapon_default_off_var.get() else "否"
                
                self.weapon_tree.item(selection[0], values=(
                    name, ammo, launch_count, launch_time, auto_engage_text, principal_text, default_off_text
                ))
                self.clear_weapon_inputs()
        
        def clear_weapon_inputs(self):
            """清空武器输入"""
            self.weapon_name_entry.delete(0, tk.END)
            self.weapon_ammo_entry.delete(0, tk.END)
            self.weapon_launch_count_entry.delete(0, tk.END)
            self.weapon_launch_time_entry.delete(0, tk.END)
            self.weapon_auto_engage_var.set(False)
            self.weapon_principal_var.set(False)
            self.weapon_default_off_var.set(False)

    # 导弹配置主框架
    class MissileFrame:
        """导弹配置主框架"""
        
        def __init__(self, parent_frame):
            self.parent_frame = parent_frame
            self.config_manager = MissileConfigManager()
            self.create_ui_components()
        
        def create_ui_components(self):
            """创建UI组件"""
            main_frame = ttk.Frame(self.parent_frame)
            main_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # 左侧配置面板
            left_frame = ttk.Frame(main_frame, width=400)
            left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
            left_frame.pack_propagate(False)
            
            # 右侧武器面板
            right_frame = ttk.Frame(main_frame, width=550)
            right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
            right_frame.pack_propagate(False)
            
            # 创建配置面板
            self.config_panel = ConfigPanel(
                left_frame, 
                self.config_manager, 
                self.on_config_select
            )
            
            # 创建武器面板
            self.weapon_panel = WeaponPanel(
                right_frame, 
                self.config_manager, 
                self.on_weapon_update
            )
        
        def on_config_select(self, config_id):
            """配置选择回调"""
            # 获取配置的实际ID
            config_name = self.config_panel.config_tree.item(config_id)['text']
            actual_config_id = self._find_config_id_by_name(config_name)
            if actual_config_id:
                self.weapon_panel.set_selected_config(actual_config_id)
            else:
                # 如果是升级项，使用升级项的名称作为配置ID
                self.weapon_panel.set_selected_config(config_id)
            
            # 确保武器面板刷新显示
            self.weapon_panel.refresh_weapon_list()
        
        def _find_config_id_by_name(self, name):
            """根据名称查找配置ID"""
            configs = self.config_manager.get_configs()
            for config_id, config in configs.items():
                if config['name'] == name:
                    return config_id
                # 检查升级项
                for improved in config['improved_by']:
                    if improved['name'] == name:
                        return f"improved_{config_id}_{improved['name']}"
            return None
        
        def on_weapon_update(self, config_id, weapon_count):
            """武器更新回调"""
            # 保存当前展开状态
            expanded_items = []
            for item in self.config_panel.config_tree.get_children():
                if self.config_panel.config_tree.item(item, 'open'):
                    expanded_items.append(item)
                    # 保存子项的展开状态
                    for child in self.config_panel.config_tree.get_children(item):
                        if self.config_panel.config_tree.item(child, 'open'):
                            expanded_items.append(child)
            
            self.config_panel.refresh_config_list()
            
            # 恢复展开状态
            for item in expanded_items:
                try:
                    self.config_panel.config_tree.item(item, open=True)
                except:
                    pass  # 如果项不存在则忽略
        
        def debug_config(self):
            """调试输出配置"""
            configs = self.config_manager.get_configs()
            has_default_output = False
            
            # 处理默认配置
            for config_id, config in configs.items():
                if config['name'] == '默认':
                    weapons = self.config_manager.get_weapons(config_id)
                    for weapon in weapons:
                        weapon_line = self._generate_weapon_line(weapon)
                        print(weapon_line)
                    has_default_output = True
                    break
            
            # 处理其他配置
            for config_id, config in configs.items():
                if config['name'] != '默认':
                    if has_default_output:
                        print()
                        has_default_output = False
                    
                    config_line = f"Config \"{config['name']}\""
                    if config['only_full']:
                        config_line += " OnlyFull"
                    if config['default']:
                        config_line += " Default"
                    print(config_line)
                    
                    weapons = self.config_manager.get_weapons(config_id)
                    for weapon in weapons:
                        weapon_line = self._generate_weapon_line(weapon)
                        print(f"    {weapon_line}")
                
                # 处理升级项
                for improved in config['improved_by']:
                    print(f"ImprovedBy \"{improved['name']}\"")
                    
                    # 查找升级项对应的武器数据
                    improved_weapons = []
                    for item_id in self.config_manager.weapon_data_dict:
                        if self.config_panel.config_tree.item(item_id)['text'] == improved['name']:
                            improved_weapons = self.config_manager.get_weapons(item_id)
                            break
                    
                    if improved_weapons:
                        for weapon in improved_weapons:
                            weapon_line = self._generate_weapon_line(weapon)
                            print(f"    {weapon_line}")
                    else:
                        print(f"    Weapon \"{improved['name']}\" 0")
        
        def _generate_weapon_line(self, weapon):
            """生成武器行"""
            weapon_line = f"Weapon \"{weapon['name']}\" {weapon['ammo']}"
            
            if weapon['launch_count'] and weapon['launch_time']:
                weapon_line += f" Launch {weapon['launch_count']} Time {weapon['launch_time']}"
            
            if weapon['auto_engage']:
                weapon_line += " AutoEngage"
            if weapon['principal']:
                weapon_line += " Principal"
            if weapon['default_off']:
                weapon_line += " DefaultOff"
                
            return weapon_line

    # 创建导弹配置界面实例
    missile_app = MissileFrame(missileFrame)

    # 导弹配置输出数据
    missileConfigData = tk.StringVar()

    def missileOutputTable():
        """输出导弹配置数据"""
        configs = missile_app.config_manager.get_configs()
        if not configs:
            missileConfigData.set("")
            return ""
        
        output_data = ""
        has_default_output = False
        
        # 处理默认配置
        for config_id, config in configs.items():
            if config['name'] == '默认':
                weapons = missile_app.config_manager.get_weapons(config_id)
                for weapon in weapons:
                    weapon_line = missile_app._generate_weapon_line(weapon)
                    output_data += f"    {weapon_line}\n"
                has_default_output = True
                break
        
        # 处理其他配置
        for config_id, config in configs.items():
            if config['name'] != '默认':
                if has_default_output:
                    output_data += "\n"
                    has_default_output = False
                
                config_line = f"    Config \"{config['name']}\""
                if config['only_full']:
                    config_line += " OnlyFull"
                if config['default']:
                    config_line += " Default"
                output_data += f"{config_line}\n"
                
                weapons = missile_app.config_manager.get_weapons(config_id)
                for weapon in weapons:
                    weapon_line = missile_app._generate_weapon_line(weapon)
                    output_data += f"        {weapon_line}\n"
            
            # 处理升级项
            for improved in config['improved_by']:
                output_data += f"        ImprovedBy \"{improved['name']}\"\n"
                
                # 查找升级项对应的武器数据
                improved_config_id = f"improved_{config_id}_{improved['name']}"
                improved_weapons = missile_app.config_manager.get_weapons(improved_config_id)
                
                if improved_weapons:
                    for weapon in improved_weapons:
                        weapon_line = missile_app._generate_weapon_line(weapon)
                        output_data += f"            {weapon_line}\n"
                else:
                    output_data += f"            Weapon \"{improved['name']}\" 0\n"
        
        missileConfigData.set(f"{output_data}")
        print(f"{missileConfigData.get()}")
        return output_data





    
#
#    missileTableData = tk.StringVar()
#
#    def missileAddToTable():
#        if missileEntry1.get().strip():
#            missileTable.insert("", tk.END, values=(
#                missileEntry1.get(),
#                missileEntry2.get(),
#                missileEntry3.get(),
#                missileEntry4.get(),
#                missileEntry5.get(),
#                missileEntry6.get(),
#                missileEntry7.get(),
#                "√" if missileCheckbox1.get() else "",
#                "√" if missileCheckbox2.get() else "",
#                missileEntry8.get()
#            ))
#            missileEntry1.delete(0, tk.END)
#            missileEntry2.delete(0, tk.END)
#            missileEntry3.delete(0, tk.END)
#            missileEntry4.delete(0, tk.END)
#            missileEntry5.delete(0, tk.END)
#            missileEntry6.delete(0, tk.END)
#            missileEntry7.delete(0, tk.END)
#            missileEntry8.delete(0, tk.END)
#            missileCheckbox1.set(False)
#            missileCheckbox2.set(False)
#
#    def missileDeleteSelected():
#        selected = missileTable.selection()
#        if selected:
#            missileTable.delete(selected[0])
#
#    def missileOutputTable():
#        items = missileTable.get_children()
#        if not items:
#            print("导弹配置表格为空")
#            missileTableData.set("")
#            return ""
#        table_data = ""
#        for item in items:
#            values = missileTable.item(item, 'values')
#            if values:
#                config_name = values[0] if len(values) > 0 else ""
#                default_config = values[1] if len(values) > 1 else ""
#                upgrade_from = values[2] if len(values) > 2 else ""
#                weapon_name = values[3] if len(values) > 3 else ""
#                ammo_count = values[4] if len(values) > 4 else ""
#                launch_count = values[5] if len(values) > 5 else ""
#                launch_interval = values[6] if len(values) > 6 else ""
#                auto_engage = values[7] if len(values) > 7 else ""
#                show_ammo = values[8] if len(values) > 8 else ""
#                modifier = values[9] if len(values) > 9 else ""
#                
#                # 构建导弹配置字符串
#                missile_config = f"    Config \"{config_name}\""
#                if default_config:
#                    missile_config += f" DefaultConfig \"{default_config}\""
#                if upgrade_from:
#                    missile_config += f" UpgradeFrom \"{upgrade_from}\""
#                if weapon_name:
#                    missile_config += f" Weapon \"{weapon_name}\""
#                if ammo_count:
#                    missile_config += f" AmmoCount {ammo_count}"
#                if launch_count:
#                    missile_config += f" LaunchCount {launch_count}"
#                if launch_interval:
#                    missile_config += f" LaunchInterval {launch_interval}"
#                if auto_engage == "√":
#                    missile_config += " AutoEngage"
#                if show_ammo == "√":
#                    missile_config += " ShowAmmo"
#                if modifier:
#                    missile_config += f" Modifier {modifier}"
#                
#                table_data += missile_config + "\n"
#        missileTableData.set(table_data)
#        print(missileTableData.get())
#        return table_data
#
#    def missileMapToEntries():
#        selected = missileTable.selection()
#        if selected:
#            values = missileTable.item(selected[0], 'values')
#            missileEntry1.delete(0, tk.END)
#            missileEntry2.delete(0, tk.END)
#            missileEntry3.delete(0, tk.END)
#            missileEntry4.delete(0, tk.END)
#            missileEntry5.delete(0, tk.END)
#            missileEntry6.delete(0, tk.END)
#            missileEntry7.delete(0, tk.END)
#            missileEntry8.delete(0, tk.END)
#            if values:
#                missileEntry1.insert(0, values[0] if len(values) > 0 else "")
#                missileEntry2.insert(0, values[1] if len(values) > 1 else "")
#                missileEntry3.insert(0, values[2] if len(values) > 2 else "")
#                missileEntry4.insert(0, values[3] if len(values) > 3 else "")
#                missileEntry5.insert(0, values[4] if len(values) > 4 else "")
#                missileEntry6.insert(0, values[5] if len(values) > 5 else "")
#                missileEntry7.insert(0, values[6] if len(values) > 6 else "")
#                missileEntry8.insert(0, values[9] if len(values) > 9 else "")
#                missileCheckbox1.set(values[7] == "√" if len(values) > 7 else False)
#                missileCheckbox2.set(values[8] == "√" if len(values) > 8 else False)
#
#    def missileSaveToCurrentRow():
#        selected = missileTable.selection()
#        if not selected:
#            missileAddToTable()  # 无选中行则添加新行
#        else:
#            missileTable.item(selected[0], values=(
#                missileEntry1.get(),
#                missileEntry2.get(),
#                missileEntry3.get(),
#                missileEntry4.get(),
#                missileEntry5.get(),
#                missileEntry6.get(),
#                missileEntry7.get(),
#                "√" if missileCheckbox1.get() else "",
#                "√" if missileCheckbox2.get() else "",
#                missileEntry8.get()
#            ))
#            missileEntry1.delete(0, tk.END)
#            missileEntry2.delete(0, tk.END)
#            missileEntry3.delete(0, tk.END)
#            missileEntry4.delete(0, tk.END)
#            missileEntry5.delete(0, tk.END)
#            missileEntry6.delete(0, tk.END)
#            missileEntry7.delete(0, tk.END)
#            missileEntry8.delete(0, tk.END)
#            missileCheckbox1.set(False)
#            missileCheckbox2.set(False)
#
#    # 创建导弹配置表格的框架
#    missileSheetFrame = ttk.Frame(missileFrame)
#    missileSheetFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
#
#    # 输入控件区域
#    missileEntryFrame = ttk.Frame(missileSheetFrame)
#    missileEntryFrame.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
#
#    # 第一行输入控件
#    ttk.Label(missileEntryFrame, text="配置名称:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
#    missileEntry1 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry1.grid(row=0, column=1, padx=5, pady=2)
#
#    ttk.Label(missileEntryFrame, text="默认配置:").grid(row=0, column=2, padx=5, pady=2, sticky="w")
#    missileEntry2 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry2.grid(row=0, column=3, padx=5, pady=2)
#
#    ttk.Label(missileEntryFrame, text="升级自:").grid(row=0, column=4, padx=5, pady=2, sticky="w")
#    missileEntry3 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry3.grid(row=0, column=5, padx=5, pady=2)
#
#    ttk.Label(missileEntryFrame, text="武器名称:").grid(row=0, column=6, padx=5, pady=2, sticky="w")
#    missileEntry4 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry4.grid(row=0, column=7, padx=5, pady=2)
#
#    # 第二行输入控件
#    ttk.Label(missileEntryFrame, text="备弹数量:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
#    missileEntry5 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry5.grid(row=1, column=1, padx=5, pady=2)
#
#    ttk.Label(missileEntryFrame, text="发射数量:").grid(row=1, column=2, padx=5, pady=2, sticky="w")
#    missileEntry6 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry6.grid(row=1, column=3, padx=5, pady=2)
#
#    ttk.Label(missileEntryFrame, text="发射间隔:").grid(row=1, column=4, padx=5, pady=2, sticky="w")
#    missileEntry7 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry7.grid(row=1, column=5, padx=5, pady=2)
#
#    ttk.Label(missileEntryFrame, text="修改器:").grid(row=1, column=6, padx=5, pady=2, sticky="w")
#    missileEntry8 = ttk.Entry(missileEntryFrame, width=15)
#    missileEntry8.grid(row=1, column=7, padx=5, pady=2)
#
#    # 第三行复选框
#    missileCheckbox1 = tk.BooleanVar()
#    missileCheckbox2 = tk.BooleanVar()
#    ttk.Checkbutton(missileEntryFrame, text="自动交战", variable=missileCheckbox1).grid(row=2, column=0, padx=5, pady=2, sticky="w")
#    ttk.Checkbutton(missileEntryFrame, text="显示备弹", variable=missileCheckbox2).grid(row=2, column=1, padx=5, pady=2, sticky="w")
#
#    # 创建导弹配置表格
#    missileTable = ttk.Treeview(missileSheetFrame, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10"), show="headings", height=12)
#    missileTable.heading("col1", text="配置名称")
#    missileTable.heading("col2", text="默认配置")
#    missileTable.heading("col3", text="升级自")
#    missileTable.heading("col4", text="武器名称")
#    missileTable.heading("col5", text="备弹数量")
#    missileTable.heading("col6", text="发射数量")
#    missileTable.heading("col7", text="发射间隔")
#    missileTable.heading("col8", text="自动交战")
#    missileTable.heading("col9", text="显示备弹")
#    missileTable.heading("col10", text="修改器")
#    
#    missileTable.column("col1", width=100)
#    missileTable.column("col2", width=80)
#    missileTable.column("col3", width=80)
#    missileTable.column("col4", width=100)
#    missileTable.column("col5", width=70)
#    missileTable.column("col6", width=70)
#    missileTable.column("col7", width=70)
#    missileTable.column("col8", width=70)
#    missileTable.column("col9", width=70)
#    missileTable.column("col10", width=80)
#
#    missileTable.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
#
#    # 创建滚动条
#    missileScrollbar = ttk.Scrollbar(missileSheetFrame, orient="vertical", command=missileTable.yview)
#    missileTable.configure(yscrollcommand=missileScrollbar.set)
#    missileScrollbar.grid(row=1, column=1, padx=(0, 5), pady=5, sticky="ns")
#
#    # 按钮区域
#    missileButtonFrame = ttk.Frame(missileSheetFrame)
#    missileButtonFrame.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
#
#    ttk.Button(missileButtonFrame, text="添加", command=missileAddToTable, width=8).grid(row=0, column=0, padx=5, pady=5)
#    ttk.Button(missileButtonFrame, text="删除", command=missileDeleteSelected, width=8).grid(row=0, column=1, padx=5, pady=5)
#    ttk.Button(missileButtonFrame, text="读取", command=missileMapToEntries, width=8).grid(row=0, column=2, padx=5, pady=5)
#    ttk.Button(missileButtonFrame, text="保存", command=missileSaveToCurrentRow, width=8).grid(row=0, column=3, padx=5, pady=5)
#    ttk.Button(missileButtonFrame, text="输出", command=missileOutputTable, width=8).grid(row=0, column=4, padx=5, pady=5)
#
#    # 配置网格权重
#    missileSheetFrame.grid_rowconfigure(1, weight=1)
#    missileSheetFrame.grid_columnconfigure(0, weight=1)
#    missileFrame.grid_rowconfigure(0, weight=1)
#    missileFrame.grid_columnconfigure(0, weight=1)

    






















    #单位数据标签页
    tabUnitData = ttk.Frame(notebook)
    notebook.add(tabUnitData, text="测试2")

    #ass = tk.Label(tabUnitData, text="饿饿饿\n啊啊啊")
    #ass.pack()






















    def cleanNameString():
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
        producesTableData.set("")
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
        for item in producesTable.get_children():
            producesTable.delete(item)
        for item in producesTable.get_children():
            producesTable.delete(item)
        for item in airwayTable.get_children():
            airwayTable.delete(item)   
        for item in canHostAircraftsTable.get_children():
            canHostAircraftsTable.delete(item)
        # 清空导弹配置数据
        missile_app.config_manager.config_data_dict.clear()
        missile_app.config_manager.weapon_data_dict.clear()
        missile_app.config_manager.initialize_default_config()
        missile_app.config_panel.refresh_config_list()
        missile_app.weapon_panel.refresh_weapon_list()

    #取消按钮
    def cancelNameString():
        askFillDefault = messagebox.askokcancel("清除当前值", "是否确认清除当前值？此操作不可撤销。")
        if askFillDefault:
            cleanNameString()
    


    #    print(globalNameEntry.get())
    #    print(techEntry.get())
    # 创建按钮容器框架


    # 使用 grid 布局让按钮在右下角横排
    

    #应用按钮
    def fillDefault():
        askFillDefault = messagebox.askokcancel("填充默认值", "是否确认填充默认值？这将覆盖当前所有输入内容，此操作不可撤销。")
        booleanCheckBoxCommand()
        if askFillDefault:
            cleanNameString()
            globalNameEntry.set("NameExample")
            techEntry.set("U_TechExample")
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
            customTable.insert("", tk.END, values=("TestOption1", "Value1"))
            customTable.insert("", tk.END, values=("TestOption2", "Value2"))

            for item in producesTable.get_children():
                producesTable.delete(item)
            producesTable.insert("", tk.END, values=("SubUnit1"))
            producesTable.insert("", tk.END, values=("SubUnit2"))

            for item in canCarryUnitTable.get_children():
                canCarryUnitTable.delete(item)
            canCarryUnitTable.insert("", tk.END, values=("SubUnit3"))
            canCarryUnitTable.insert("", tk.END, values=("SubUnit4"))

            for item in airwayTable.get_children():
                airwayTable.delete(item)
            airwayTable.insert("", tk.END, values=("2", "60"))
            airwayTable.insert("", tk.END, values=("1", "180"))

            for item in canHostAircraftsTable.get_children():
                canHostAircraftsTable.delete(item)
            canHostAircraftsTable.insert("", tk.END, values=("SubUnit5", "15", "", "2"))
            canHostAircraftsTable.insert("", tk.END, values=("SubUnit6", "10", "1", "5", "√"))

            # 添加导弹配置默认数据
            config1_id = missile_app.config_manager.add_config("Config1")
            missile_app.config_manager.add_weapon(config1_id, {
                'name': 'HMG', 'ammo': '20000', 'launch_count': '2', 'launch_time': '1',
                'auto_engage': True, 'principal': True, 'default_off': False
            })
            missile_app.config_manager.add_weapon(config1_id, {
                'name': 'Bomb', 'ammo': '5', 'launch_count': '', 'launch_time': '',
                'auto_engage': False, 'principal': True, 'default_off': False
            })

            config2_id = missile_app.config_manager.add_config("Config2", only_full=True, default=True)
            missile_app.config_manager.add_improved_by("Config2", "Tech1")
            missile_app.config_manager.add_improved_by("Config2", "Tech2")
            missile_app.config_manager.add_improved_by("Config2", "Tech3")
            
            # 为升级项添加武器
            missile_app.config_manager.add_weapon("improved_config2_Tech1", {
                'name': 'Weapon1', 'ammo': '1', 'launch_count': '', 'launch_time': '',
                'auto_engage': False, 'principal': False, 'default_off': False
            })
            missile_app.config_manager.add_weapon("improved_config2_Tech2", {
                'name': 'Weapon2', 'ammo': '2', 'launch_count': '', 'launch_time': '',
                'auto_engage': False, 'principal': False, 'default_off': False
            })
            missile_app.config_manager.add_weapon("improved_config2_Tech3", {
                'name': 'Weapon3', 'ammo': '3', 'launch_count': '', 'launch_time': '',
                'auto_engage': False, 'principal': False, 'default_off': False
            })

            missile_app.config_panel.refresh_config_list()


    #生成代码按钮

    
    #生成代码段
    def generateCode():
        # 先把各项检查并生成对应的 StringVar 内容
        checkBasicData()
        producesOutputTable()  # 确保生产单位表格数据已更新
        airwayOutputTable()
        canHostAircraftsOutputTable()
        canCarryUnitOutputTable()
        missileOutputTable()  # 确保导弹配置表格数据已更新

        # 检查必填字段是否已填写

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
            f"{producesTableData.get()}"
            f"{canCarryUnitTableData.get()}"
            f"\n"
            f"{behaviorString.get()}"
            f"{airwayTableData.get()}"
            f"{canHostAircraftsTableData.get()}"
            f"{missileConfigData.get()}"  # 使用导弹配置数据
            f"\n"
            
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
        ("HangarSpaceRequired", hangarSpaceRequiredEntry, hangarSpaceRequiredString, "Normal"),
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
        customOutputTable()
        canCarryUnitOutputTable()
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




    
    












    # 创建全局按钮框架（在所有标签页中共享，位于右下角）
    globalButtonFrame = ttk.Frame(mainFrame)
    globalButtonFrame.pack(side="bottom", anchor="se", padx=5, pady=5)
    
    ttk.Button(globalButtonFrame, command=cancelNameString, text="清除").pack(side="left", padx=5)
    ttk.Button(globalButtonFrame, command=fillDefault, text="默认").pack(side="left", padx=5)
    ttk.Button(globalButtonFrame, command=generateCode, text="生成").pack(side="left", padx=5)
    ttk.Button(globalButtonFrame, command=missileOutputTable, text="debug").pack(side="left", padx=5)

    screenSize = root.maxsize()
    print(screenSize)
    Width, High = screenSize


    root.geometry(f"1024x768+{int(Width*.5-512)}+{int(High*.5-384)}")
    root.resizable(False, False)

    root.mainloop()

if __name__ == "__main__":
    main()
