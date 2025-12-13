# -*- coding: utf-8 -*-
"""
ICBM: Escalation Unit Code Generator
单位代码生成器 - 主程序文件
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json
import csv
import os

# ============================================================================
# 多语言支持模块
# ============================================================================

class LanguageManager:
    """多语言管理器"""
    
    def __init__(self):
        self.CurrentLanguage = "zh_CN"
        self.Translations = {}
        self.LoadLanguageFiles()
    
    def LoadLanguageFiles(self):
        """加载语言文件"""
        LanguageDir = os.path.join(os.path.dirname(__file__), "Languages")
        if not os.path.exists(LanguageDir):
            os.makedirs(LanguageDir)
            self.CreateDefaultLanguageFiles(LanguageDir)
        
        for FileName in os.listdir(LanguageDir):
            if FileName.endswith(".json"):
                LangCode = FileName.replace(".json", "")
                FilePath = os.path.join(LanguageDir, FileName)
                try:
                    with open(FilePath, "r", encoding="utf-8") as f:
                        self.Translations[LangCode] = json.load(f)
                except Exception as e:
                    print(f"加载语言文件失败: {FileName}, 错误: {e}")
    
    def CreateDefaultLanguageFiles(self, LanguageDir):
        """创建默认语言文件"""
        # 中文语言文件
        ZhCN = {
            "AppTitle": "ICBM: Escalation 单位代码生成器",
            "Tab_BasicInfo": "基本信息",
            "Tab_Behavior": "行为控制",
            "Tab_SubUnit": "子单位/生产",
            "Tab_Weapon": "武器配置",
            "Tab_RadarModifier": "雷达/修改器",
            "Tab_StateSwitch": "状态切换",
            "Tab_Upgrade": "升级项",
            "Group_BasicData": "基础数据",
            "Group_PropertyData": "属性数据",
            "Group_CustomParams": "自定义参数",
            "Label_GlobalName": "全局名称:",
            "Label_Tech": "科技引用:",
            "Label_Type": "单位类型:",
            "Label_Class": "单位分组:",
            "Label_Movie": "俯视图路径:",
            "Label_AbstractMovie": "缩略图路径:",
            "Label_Model": "3D模型路径:",
            "Label_Icon": "图标路径:",
            "Label_RoundIcon": "圆形图标:",
            "Label_IconIDX": "图标索引:",
            "Label_DrawSize": "绘制大小:",
            "Label_AbstractDrawSize": "缩略绘制:",
            "Label_ModelDrawSize": "模型尺寸:",
            "Label_Sound": "音效编码:",
            "Label_LaunchMeSound": "发射音效:",
            "Label_LaunchMePathIcon": "发射图标:",
            "Label_DrawOrder": "绘制顺序:",
            "Label_Crash": "爆炸效果:",
            "Label_Power": "生命值:",
            "Label_Size": "受击体积:",
            "Label_Speed": "移动速度:",
            "Label_TurnSpeed": "转向速度:",
            "Label_Range": "航程:",
            "Label_ProductionCost": "生产成本:",
            "Label_SelfDestruct": "自毁时间:",
            "Label_MaxElevation": "最大高度:",
            "Label_MinElevation": "最小高度:",
            "Label_ResupplyRadius": "补给半径:",
            "Label_FollowRadius": "跟随半径:",
            "Label_OccupationRadius": "占领半径:",
            "Label_AutoRepair": "自动修理:",
            "Label_MaxAutoEngageRange": "自动攻击:",
            "Label_ProductionPlacementRadius": "放置半径:",
            "Label_MaxNumberOnMap": "地图最大:",
            "Label_MaxNumberToOrder": "持有最大:",
            "Label_TimeToOccupyMult": "占领时间:",
            "Label_DecayTimer": "衰减时间:",
            "Label_HangarSpaceRequired": "容量需求:",
            "Label_HangarMaxLoad": "最大容量:",
            "Btn_Add": "+",
            "Btn_Delete": "-",
            "Btn_Load": "读取选中项",
            "Btn_Save": "保存至选中项",
            "Btn_MoveUp": "↑",
            "Btn_MoveDown": "↓",
            "Btn_Clear": "清除",
            "Btn_Default": "默认",
            "Btn_Generate": "生成",
            "Btn_Import": "导入",
            "Btn_Export": "导出",
            "Col_Parameter": "参数",
            "Col_Value": "值",
            "Col_Unit": "单位",
            "Col_Count": "数量",
            "Col_Airway": "航线",
            "Col_PatrolCount": "巡逻数",
            "Col_AutoPatrol": "自巡逻",
            "Msg_ConfirmClear": "确定要清除所有数据吗？此操作不可撤销。",
            "Msg_ConfirmDefault": "确定要填充默认值吗？这将覆盖当前数据。",
            "Msg_RequiredFields": "请确保所有必填字段已填写！",
            "Msg_Success": "操作成功",
            "Msg_Error": "错误",
            "Msg_Warning": "警告"
        }
        
        # 英文语言文件
        EnUS = {
            "AppTitle": "ICBM: Escalation Unit Code Generator",
            "Tab_BasicInfo": "Basic Info",
            "Tab_Behavior": "Behavior",
            "Tab_SubUnit": "SubUnit/Production",
            "Tab_Weapon": "Weapon Config",
            "Tab_RadarModifier": "Radar/Modifier",
            "Tab_StateSwitch": "State Switch",
            "Tab_Upgrade": "Upgrades",
            "Group_BasicData": "Basic Data",
            "Group_PropertyData": "Property Data",
            "Group_CustomParams": "Custom Parameters",
            "Label_GlobalName": "Global Name:",
            "Label_Tech": "Tech Reference:",
            "Label_Type": "Unit Type:",
            "Label_Class": "Unit Class:",
            "Label_Movie": "Topdown Path:",
            "Label_AbstractMovie": "Abstract Path:",
            "Label_Model": "3D Model Path:",
            "Label_Icon": "Icon Path:",
            "Label_RoundIcon": "Round Icon:",
            "Label_IconIDX": "Icon Index:",
            "Label_DrawSize": "Draw Size:",
            "Label_AbstractDrawSize": "Abstract Size:",
            "Label_ModelDrawSize": "Model Size:",
            "Label_Sound": "Sound Code:",
            "Label_LaunchMeSound": "Launch Sound:",
            "Label_LaunchMePathIcon": "Launch Icon:",
            "Label_DrawOrder": "Draw Order:",
            "Label_Crash": "Crash Effect:",
            "Label_Power": "Power:",
            "Label_Size": "Size:",
            "Label_Speed": "Speed:",
            "Label_TurnSpeed": "Turn Speed:",
            "Label_Range": "Range:",
            "Label_ProductionCost": "Production Cost:",
            "Label_SelfDestruct": "Self Destruct:",
            "Label_MaxElevation": "Max Elevation:",
            "Label_MinElevation": "Min Elevation:",
            "Label_ResupplyRadius": "Resupply Radius:",
            "Label_FollowRadius": "Follow Radius:",
            "Label_OccupationRadius": "Occupation Radius:",
            "Label_AutoRepair": "Auto Repair:",
            "Label_MaxAutoEngageRange": "Auto Engage:",
            "Label_ProductionPlacementRadius": "Placement Radius:",
            "Label_MaxNumberOnMap": "Max On Map:",
            "Label_MaxNumberToOrder": "Max To Order:",
            "Label_TimeToOccupyMult": "Occupy Time:",
            "Label_DecayTimer": "Decay Timer:",
            "Label_HangarSpaceRequired": "Hangar Required:",
            "Label_HangarMaxLoad": "Hangar Max:",
            "Btn_Add": "+",
            "Btn_Delete": "-",
            "Btn_Load": "Load Selected",
            "Btn_Save": "Save to Selected",
            "Btn_MoveUp": "↑",
            "Btn_MoveDown": "↓",
            "Btn_Clear": "Clear",
            "Btn_Default": "Default",
            "Btn_Generate": "Generate",
            "Btn_Import": "Import",
            "Btn_Export": "Export",
            "Col_Parameter": "Parameter",
            "Col_Value": "Value",
            "Col_Unit": "Unit",
            "Col_Count": "Count",
            "Col_Airway": "Airway",
            "Col_PatrolCount": "Patrol",
            "Col_AutoPatrol": "AutoPatrol",
            "Msg_ConfirmClear": "Are you sure you want to clear all data? This cannot be undone.",
            "Msg_ConfirmDefault": "Are you sure you want to fill default values? This will overwrite current data.",
            "Msg_RequiredFields": "Please ensure all required fields are filled!",
            "Msg_Success": "Success",
            "Msg_Error": "Error",
            "Msg_Warning": "Warning"
        }
        
        # 保存语言文件
        with open(os.path.join(LanguageDir, "zh_CN.json"), "w", encoding="utf-8") as f:
            json.dump(ZhCN, f, ensure_ascii=False, indent=4)
        with open(os.path.join(LanguageDir, "en_US.json"), "w", encoding="utf-8") as f:
            json.dump(EnUS, f, ensure_ascii=False, indent=4)
        
        self.Translations["zh_CN"] = ZhCN
        self.Translations["en_US"] = EnUS
    
    def Get(self, Key):
        """获取翻译文本"""
        if self.CurrentLanguage in self.Translations:
            return self.Translations[self.CurrentLanguage].get(Key, Key)
        return Key
    
    def SetLanguage(self, LangCode):
        """设置当前语言"""
        if LangCode in self.Translations:
            self.CurrentLanguage = LangCode
            return True
        return False
    
    def GetAvailableLanguages(self):
        """获取可用语言列表"""
        return list(self.Translations.keys())


# ============================================================================
# 数据库管理模块
# ============================================================================

class DatabaseManager:
    """数据库管理器 - 用于自动补全"""
    
    def __init__(self):
        self.DatabaseDir = os.path.join(os.path.dirname(__file__), "Database")
        self.Data = {
            "Types": [],
            "Classes": [],
            "Units": [],
            "Techs": [],
            "Weapons": [],
            "Radars": [],
            "Modifiers": [],
            "Crashes": []
        }
        self.LoadDatabases()
    
    def LoadDatabases(self):
        """加载所有数据库文件"""
        if not os.path.exists(self.DatabaseDir):
            os.makedirs(self.DatabaseDir)
            self.CreateDefaultDatabases()
        
        for Category in self.Data.keys():
            FilePath = os.path.join(self.DatabaseDir, f"{Category}.csv")
            if os.path.exists(FilePath):
                try:
                    with open(FilePath, "r", encoding="utf-8") as f:
                        Reader = csv.reader(f)
                        for Row in Reader:
                            self.Data[Category] = Row
                            break  # 只读取第一行
                except Exception as e:
                    print(f"加载数据库失败: {Category}.csv, 错误: {e}")
    
    def CreateDefaultDatabases(self):
        """创建默认数据库文件"""
        DefaultData = {
            "Types": ["Ground", "Airborne", "Naval", "Subwater", "Satellite"],
            "Classes": ["UC_Ground", "UC_Airborne", "UC_Naval", "UC_Subwater", "UC_Satellite"],
            "Units": ["Infantry", "Tank", "Aircraft", "Ship", "Submarine"],
            "Techs": ["U_Infantry", "U_Tank", "U_Aircraft", "U_Ship", "U_Submarine"],
            "Weapons": ["HMG", "Cannon", "Missile", "Torpedo", "Bomb"],
            "Radars": ["Standard_Radar", "Advanced_Radar", "Spy_Camera"],
            "Modifiers": ["EMP_Killable", "EMP_Defence_Mod_1", "Stealth_Mod"],
            "Crashes": ["std_bomb", "big_bomb", "small_bomb"]
        }
        
        for Category, Values in DefaultData.items():
            FilePath = os.path.join(self.DatabaseDir, f"{Category}.csv")
            with open(FilePath, "w", encoding="utf-8", newline="") as f:
                Writer = csv.writer(f)
                Writer.writerow(Values)
            self.Data[Category] = Values
    
    def Get(self, Category):
        """获取指定类别的数据列表"""
        return self.Data.get(Category, [])
    
    def Add(self, Category, Value):
        """添加数据到指定类别"""
        if Category in self.Data and Value not in self.Data[Category]:
            self.Data[Category].append(Value)
            self.SaveCategory(Category)
    
    def SaveCategory(self, Category):
        """保存指定类别的数据"""
        FilePath = os.path.join(self.DatabaseDir, f"{Category}.csv")
        with open(FilePath, "w", encoding="utf-8", newline="") as f:
            Writer = csv.writer(f)
            Writer.writerow(self.Data[Category])


# ============================================================================
# 主应用程序类
# ============================================================================

class UnitCodeGeneratorApp:
    """单位代码生成器主应用"""
    
    def __init__(self):
        self.Root = tk.Tk()
        self.Lang = LanguageManager()
        self.DB = DatabaseManager()
        
        # 数据存储
        self.BasicInfoVars = {}
        self.BehaviorVars = {}
        self.CustomParamsData = []
        
        self.SetupWindow()
        self.CreateWidgets()
    
    def SetupWindow(self):
        """设置主窗口"""
        self.Root.title(self.Lang.Get("AppTitle"))
        
        # 获取屏幕尺寸并居中显示
        ScreenWidth = self.Root.winfo_screenwidth()
        ScreenHeight = self.Root.winfo_screenheight()
        WindowWidth = 1024
        WindowHeight = 768
        X = (ScreenWidth - WindowWidth) // 2
        Y = (ScreenHeight - WindowHeight) // 2
        
        self.Root.geometry(f"{WindowWidth}x{WindowHeight}+{X}+{Y}")
        self.Root.resizable(False, False)
    
    def CreateWidgets(self):
        """创建所有控件"""
        # 主框架
        self.MainFrame = ttk.Frame(self.Root)
        self.MainFrame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # 顶部工具栏
        self.CreateToolbar()
        
        # 标签页
        self.Notebook = ttk.Notebook(self.MainFrame)
        self.Notebook.pack(fill="both", expand=True)
        
        # 创建各个标签页
        self.CreateBasicInfoTab()
        self.CreateBehaviorTab()
        self.CreateSubUnitTab()
        self.CreateWeaponTab()
        self.CreateRadarModifierTab()
        self.CreateStateSwitchTab()
        self.CreateUpgradeTab()
        
        # 底部按钮
        self.CreateBottomButtons()
    
    def CreateToolbar(self):
        """创建工具栏"""
        ToolbarFrame = ttk.Frame(self.MainFrame)
        ToolbarFrame.pack(fill="x", pady=(0, 5))
        
        # 语言选择
        ttk.Label(ToolbarFrame, text="Language:").pack(side="left", padx=(0, 5))
        self.LanguageCombo = ttk.Combobox(
            ToolbarFrame, 
            values=self.Lang.GetAvailableLanguages(),
            width=10,
            state="readonly"
        )
        self.LanguageCombo.set(self.Lang.CurrentLanguage)
        self.LanguageCombo.pack(side="left", padx=(0, 10))
        self.LanguageCombo.bind("<<ComboboxSelected>>", self.OnLanguageChange)
        
        # 导入导出按钮
        ttk.Button(ToolbarFrame, text=self.Lang.Get("Btn_Import"), 
                   command=self.ImportConfig).pack(side="right", padx=2)
        ttk.Button(ToolbarFrame, text=self.Lang.Get("Btn_Export"), 
                   command=self.ExportConfig).pack(side="right", padx=2)
    
    def OnLanguageChange(self, Event=None):
        """语言切换事件"""
        NewLang = self.LanguageCombo.get()
        self.Lang.SetLanguage(NewLang)
        # 保存语言设置到文件
        self.SaveLanguageSettings()
        # 更新界面文本
        self.UpdateUI()
        messagebox.showinfo(
            self.Lang.Get("Msg_Success"),
            "Language changed successfully!"
        )
    
    def SaveLanguageSettings(self):
        """保存语言设置"""
        try:
            with open("language_config.json", "w", encoding="utf-8") as f:
                json.dump({"language": self.Lang.CurrentLanguage}, f)
        except Exception as e:
            print(f"保存语言设置失败: {e}")
    
    def LoadLanguageSettings(self):
        """加载语言设置"""
        try:
            if os.path.exists("language_config.json"):
                with open("language_config.json", "r", encoding="utf-8") as f:
                    config = json.load(f)
                    lang = config.get("language", "zh_CN")
                    if self.Lang.SetLanguage(lang):
                        self.LanguageCombo.set(lang)
        except Exception as e:
            print(f"加载语言设置失败: {e}")
    
    def UpdateUI(self):
        """更新界面文本（无需重启）"""
        # 更新窗口标题
        self.Root.title(self.Lang.Get("AppTitle"))
        
        # 更新标签页标题
        if hasattr(self, 'Notebook') and self.Notebook is not None:
            # 重新创建标签页标题（复杂操作，暂时跳过）
            pass
        
        # 更新按钮文本
        # 这里可以添加更多文本更新逻辑
        pass
    
    def CreateBasicInfoTab(self):
        """创建基本信息标签页"""
        Frame = ttk.Frame(self.Notebook)
        self.Notebook.add(Frame, text=self.Lang.Get("Tab_BasicInfo"))
        
        Frame.columnconfigure(0, weight=1)
        Frame.columnconfigure(1, weight=1)
        Frame.rowconfigure(0, weight=1)
        Frame.rowconfigure(1, weight=1)
        
        # 基础数据组
        self.CreateBasicDataGroup(Frame)
        
        # 属性数据组
        self.CreatePropertyDataGroup(Frame)
        
        # 自定义参数组
        self.CreateCustomParamsGroup(Frame)
    
    def CreateBasicDataGroup(self, ParentFrame):
        """创建基础数据组"""
        GroupFrame = ttk.LabelFrame(ParentFrame, text=self.Lang.Get("Group_BasicData"))
        GroupFrame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        
        # 第一列字段
        Col1Fields = [
            ("GlobalName", "Label_GlobalName", "entry", None),
            ("Tech", "Label_Tech", "combo", "Techs"),
            ("Movie", "Label_Movie", "entry", None),
            ("AbstractMovie", "Label_AbstractMovie", "entry", None),
            ("Model", "Label_Model", "entry", None),
            ("Icon", "Label_Icon", "entry", None),
            ("RoundIcon", "Label_RoundIcon", "entry", None),
            ("LaunchMePathIcon", "Label_LaunchMePathIcon", "entry", None)
        ]
        
        for i, (Key, LabelKey, WidgetType, DbKey) in enumerate(Col1Fields):
            ttk.Label(GroupFrame, text=self.Lang.Get(LabelKey)).grid(
                row=i, column=0, padx=10, pady=5, sticky="w"
            )
            Var = tk.StringVar()
            self.BasicInfoVars[Key] = Var
            
            if WidgetType == "combo" and DbKey:
                Widget = ttk.Combobox(GroupFrame, textvariable=Var, 
                                      values=self.DB.Get(DbKey), width=25)
            else:
                Widget = ttk.Entry(GroupFrame, textvariable=Var, width=60)
            Widget.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        
        # 第二列字段
        Col2Fields = [
            ("Type", "Label_Type", "combo", "Types"),
            ("Crash", "Label_Crash", "combo", "Crashes"),
            ("Class", "Label_Class", "combo", "Classes"),
            ("DrawSize", "Label_DrawSize", "entry", None),
            ("AbstractDrawSize", "Label_AbstractDrawSize", "entry", None),
            ("Sound", "Label_Sound", "entry", None),
            ("LaunchMeSound", "Label_LaunchMeSound", "entry", None),
            ("IconIDX", "Label_IconIDX", "entry", None)
        ]
        
        for i, (Key, LabelKey, WidgetType, DbKey) in enumerate(Col2Fields):
            ttk.Label(GroupFrame, text=self.Lang.Get(LabelKey)).grid(
                row=i, column=2, padx=10, pady=5, sticky="w"
            )
            Var = tk.StringVar()
            self.BasicInfoVars[Key] = Var
            
            if WidgetType == "combo" and DbKey:
                Widget = ttk.Combobox(GroupFrame, textvariable=Var, 
                                      values=self.DB.Get(DbKey), width=18)
            else:
                Widget = ttk.Entry(GroupFrame, textvariable=Var, width=20)
            Widget.grid(row=i, column=3, padx=10, pady=5, sticky="w")
    
    def CreatePropertyDataGroup(self, ParentFrame):
        """创建属性数据组"""
        GroupFrame = ttk.LabelFrame(ParentFrame, text=self.Lang.Get("Group_PropertyData"))
        GroupFrame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        # 属性字段 - 第一列
        Col1Fields = [
            ("Power", "Label_Power"),
            ("TurnSpeed", "Label_TurnSpeed"),
            ("Speed", "Label_Speed"),
            ("Range", "Label_Range"),
            ("Size", "Label_Size"),
            ("ProductionCost", "Label_ProductionCost"),
            ("SelfDestruct", "Label_SelfDestruct"),
            ("AutoRepair", "Label_AutoRepair"),
            ("ResupplyRadius", "Label_ResupplyRadius"),
            ("MaxAutoEngageRange", "Label_MaxAutoEngageRange")
        ]
        
        for i, (Key, LabelKey) in enumerate(Col1Fields):
            ttk.Label(GroupFrame, text=self.Lang.Get(LabelKey)).grid(
                row=i, column=0, padx=10, pady=5, sticky="w"
            )
            Var = tk.StringVar()
            self.BasicInfoVars[Key] = Var
            Entry = ttk.Entry(GroupFrame, textvariable=Var, width=15)
            Entry.grid(row=i, column=1, padx=10, pady=5)
        
        # 属性字段 - 第二列
        Col2Fields = [
            ("FollowRadius", "Label_FollowRadius"),
            ("OccupationRadius", "Label_OccupationRadius"),
            ("MaxElevation", "Label_MaxElevation"),
            ("MinElevation", "Label_MinElevation"),
            ("ProductionPlacementRadius", "Label_ProductionPlacementRadius"),
            ("DrawOrder", "Label_DrawOrder"),
            ("MaxNumberOnMap", "Label_MaxNumberOnMap"),
            ("MaxNumberToOrder", "Label_MaxNumberToOrder"),
            ("HangarSpaceRequired", "Label_HangarSpaceRequired"),
            ("HangarMaxLoad", "Label_HangarMaxLoad")
        ]
        
        for i, (Key, LabelKey) in enumerate(Col2Fields):
            ttk.Label(GroupFrame, text=self.Lang.Get(LabelKey)).grid(
                row=i, column=2, padx=10, pady=5, sticky="w"
            )
            Var = tk.StringVar()
            self.BasicInfoVars[Key] = Var
            Entry = ttk.Entry(GroupFrame, textvariable=Var, width=15)
            Entry.grid(row=i, column=3, padx=10, pady=5)
    
    def CreateCustomParamsGroup(self, ParentFrame):
        """创建自定义参数组"""
        GroupFrame = ttk.LabelFrame(ParentFrame, text=self.Lang.Get("Group_CustomParams"))
        GroupFrame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        
        # 输入框架
        InputFrame = ttk.Frame(GroupFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(InputFrame, text=self.Lang.Get("Col_Parameter") + ":").grid(
            row=0, column=0, padx=5, pady=2, sticky="w"
        )
        self.CustomParamNameEntry = ttk.Entry(InputFrame, width=18)
        self.CustomParamNameEntry.grid(row=1, column=0, padx=5, pady=2)
        
        ttk.Label(InputFrame, text=self.Lang.Get("Col_Value") + ":").grid(
            row=0, column=1, padx=5, pady=2, sticky="w"
        )
        self.CustomParamValueEntry = ttk.Entry(InputFrame, width=18)
        self.CustomParamValueEntry.grid(row=1, column=1, padx=5, pady=2)
        
        # 表格
        TableFrame = ttk.Frame(GroupFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.CustomParamsTable = ttk.Treeview(
            TableFrame, 
            columns=("Parameter", "Value"), 
            show="headings", 
            height=12
        )
        self.CustomParamsTable.heading("Parameter", text=self.Lang.Get("Col_Parameter"))
        self.CustomParamsTable.heading("Value", text=self.Lang.Get("Col_Value"))
        self.CustomParamsTable.column("Parameter", width=140)
        self.CustomParamsTable.column("Value", width=140)
        
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", 
                                   command=self.CustomParamsTable.yview)
        self.CustomParamsTable.configure(yscrollcommand=Scrollbar.set)
        
        self.CustomParamsTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        # 按钮框架
        ButtonFrame = ttk.Frame(GroupFrame)
        ButtonFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Add"), width=3,
                   command=self.AddCustomParam).pack(side="left", padx=2)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Delete"), width=3,
                   command=self.DeleteCustomParam).pack(side="left", padx=2)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Load"), width=10,
                   command=self.LoadCustomParam).pack(side="left", padx=2)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Save"), width=12,
                   command=self.SaveCustomParam).pack(side="left", padx=2)
    
    def AddCustomParam(self):
        """添加自定义参数"""
        Name = self.CustomParamNameEntry.get().strip()
        Value = self.CustomParamValueEntry.get().strip()
        if Name:
            self.CustomParamsTable.insert("", tk.END, values=(Name, Value))
            self.CustomParamNameEntry.delete(0, tk.END)
            self.CustomParamValueEntry.delete(0, tk.END)
    
    def DeleteCustomParam(self):
        """删除选中的自定义参数"""
        Selected = self.CustomParamsTable.selection()
        if Selected:
            self.CustomParamsTable.delete(Selected[0])
    
    def LoadCustomParam(self):
        """读取选中的自定义参数"""
        Selected = self.CustomParamsTable.selection()
        if Selected:
            Values = self.CustomParamsTable.item(Selected[0], "values")
            self.CustomParamNameEntry.delete(0, tk.END)
            self.CustomParamValueEntry.delete(0, tk.END)
            if Values:
                self.CustomParamNameEntry.insert(0, Values[0])
                if len(Values) > 1:
                    self.CustomParamValueEntry.insert(0, Values[1])
    
    def SaveCustomParam(self):
        """保存到选中的自定义参数"""
        Selected = self.CustomParamsTable.selection()
        Name = self.CustomParamNameEntry.get().strip()
        Value = self.CustomParamValueEntry.get().strip()
        
        if not Selected:
            self.AddCustomParam()
        else:
            self.CustomParamsTable.item(Selected[0], values=(Name, Value))
            self.CustomParamNameEntry.delete(0, tk.END)
            self.CustomParamValueEntry.delete(0, tk.END)
    
    def CreateBehaviorTab(self):
        """创建行为控制标签页"""
        Frame = ttk.Frame(self.Notebook)
        self.Notebook.add(Frame, text=self.Lang.Get("Tab_Behavior"))
        
        Frame.columnconfigure(0, weight=1)
        Frame.rowconfigure(0, weight=1)
        
        # 行为控制组
        GroupFrame = ttk.LabelFrame(Frame, text="行为控制")
        GroupFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # 行为选项定义：(变量名, 显示文本, 代码键名, 类型, 隐藏规则)
        # 类型: Boolean=输出Yes/No, Existed=勾选时只输出键名
        # 隐藏规则: Normal=总是输出, HideWhenFalse=False时不输出
        self.BehaviorOptions = [
            ("AlwaysVisibleOnEnemyTerritory", "在敌方领土可见", "AlwaysVisibleOnEnemyTerritory", "Boolean", "Normal"),
            ("DoesNotTriggerWarWhenAttacked", "受击不触发战争", "DoesNotTriggerWarWhenAttacked", "Boolean", "HideWhenFalse"),
            ("CanCrossBorderDuringPeaceTime", "和平时期可跨越边界", "CanCrossBorderDuringPeaceTime", "Boolean", "Normal"),
            ("CanCrossBorder", "可跨越边界", "CanCrossBorder", "Boolean", "Normal"),
            ("DoesNotTriggerWarOnAttack", "攻击不触发战争", "DoesNotTriggerWarOnAttack", "Boolean", "HideWhenFalse"),
            ("ReportAsHosted", "显示被装载于母单位", "ReportAsHosted", "Boolean", "HideWhenFalse"),
            ("TargetInPlanner", "在被攻击名单中", "TargetInPlanner", "Boolean", "HideWhenFalse"),
            ("AttackerInPlanner", "在攻击者名单中", "AttackerInPlanner", "Existed", "HideWhenFalse"),
            ("CanAccessGlobalStorage", "可访问全局库存", "CanAccessGlobalStorage", "Boolean", "HideWhenFalse"),
            ("CanAccessWeaponStockpile", "可访问武器库存", "CanAccessWeaponStockpile", "Boolean", "HideWhenFalse"),
            ("CanAccessUnitStockpile", "可访问单位库存", "CanAccessUnitStockpile", "Boolean", "HideWhenFalse"),
            ("CanHangInTheAir", "可悬停", "CanHangInTheAir", "Boolean", "HideWhenFalse"),
            ("HideOwnership", "隐藏所有者阵营", "HideOwnership", "Boolean", "HideWhenFalse"),
            ("CanPatrolPoint", "空中单位巡逻点", "CanPatrolPoint", "Boolean", "HideWhenFalse"),
            ("AutoReturn", "自动返回母单位", "AutoReturn", "Boolean", "HideWhenFalse"),
            ("ProducedByAnotherUnit", "由其他单位生产", "ProducedByAnotherUnit", "Boolean", "HideWhenFalse"),
            ("FixedRotationAngle", "固定朝向", "FixedRotationAngle", "Boolean", "HideWhenFalse"),
            ("AttackOnMove", "移动时可攻击", "AttackOnMove", "Boolean", "HideWhenFalse"),
            ("ShowDisabledOnDeploymentMarker", "部署时显示禁用", "ShowDisabledOnDeploymentMarker", "Boolean", "HideWhenFalse"),
            ("DestroyOnFactionSurrender", "投降后自动摧毁", "DestroyOnFactionSurrender", "Boolean", "HideWhenFalse"),
            ("HiddenFromAllies", "对盟友隐藏", "HiddenFromAllies", "Existed", "HideWhenFalse"),
            ("AttackIfDestroyed", "被摧毁时反击", "AttackIfDestroyed", "Existed", "HideWhenFalse"),
            ("NoAutoAttack", "不自动攻击", "NoAutoAttack", "Existed", "HideWhenFalse"),
            ("NoAutoAttackSub", "不自动攻击潜艇", "NoAutoAttackSub", "Existed", "HideWhenFalse"),
            ("Slave", "附属于母单位", "Slave", "Boolean", "HideWhenFalse"),
            ("NoAutoDeploy", "不自动部署", "NoAutoDeploy", "Boolean", "HideWhenFalse"),
            ("ExecuteOrdersWhenBesieged", "被围困时执行命令", "ExecuteOrdersWhenBesieged", "Boolean", "HideWhenFalse"),
            ("HideAbstract", "隐藏缩略图", "HideAbstract", "Boolean", "HideWhenFalse")
        ]
        
        # 创建复选框
        self.BehaviorVars = {}
        ColCount = 3  # 每行显示3个
        for i, (VarName, DisplayText, CodeKey, BType, HideRule) in enumerate(self.BehaviorOptions):
            Row = i // ColCount
            Col = i % ColCount
            
            Var = tk.BooleanVar()
            self.BehaviorVars[VarName] = {
                "Var": Var,
                "CodeKey": CodeKey,
                "Type": BType,
                "HideRule": HideRule
            }
            
            Checkbox = ttk.Checkbutton(GroupFrame, text=DisplayText, variable=Var)
            Checkbox.grid(row=Row, column=Col, padx=15, pady=5, sticky="w")
    
    def CreateSubUnitTab(self):
        """创建子单位/生产标签页"""
        Frame = ttk.Frame(self.Notebook)
        self.Notebook.add(Frame, text=self.Lang.Get("Tab_SubUnit"))
        
        Frame.columnconfigure(0, weight=1)
        Frame.columnconfigure(1, weight=1)
        Frame.columnconfigure(2, weight=2)
        Frame.rowconfigure(0, weight=1)
        Frame.rowconfigure(1, weight=1)
        
        # 生产单位表格
        self.CreateProducesGroup(Frame)
        # 可搭载单位表格
        self.CreateCanCarryGroup(Frame)
        # 航线表格
        self.CreateAirwayGroup(Frame)
        # 子单位表格
        self.CreateCanHostAircraftsGroup(Frame)
    
    def CreateProducesGroup(self, ParentFrame):
        """创建生产单位组"""
        GroupFrame = ttk.LabelFrame(ParentFrame, text="允许生产的单位")
        GroupFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(GroupFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(InputFrame, text="单位:").pack(side="left", padx=2)
        self.ProducesEntry = ttk.Combobox(InputFrame, values=self.DB.Get("Units"), width=22)
        self.ProducesEntry.pack(side="left", padx=2)
        ttk.Button(InputFrame, text="+", width=3, 
                   command=self.AddProduces).pack(side="left", padx=2)
        ttk.Button(InputFrame, text="-", width=3,
                   command=self.DeleteProduces).pack(side="left", padx=2)
        
        # 表格
        TableFrame = ttk.Frame(GroupFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.ProducesTable = ttk.Treeview(TableFrame, columns=("Unit",), show="headings", height=8)
        self.ProducesTable.heading("Unit", text="单位")
        self.ProducesTable.column("Unit", width=200)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.ProducesTable.yview)
        self.ProducesTable.configure(yscrollcommand=Scrollbar.set)
        self.ProducesTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        # 按钮
        BtnFrame = ttk.Frame(GroupFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text="读取", width=8, command=self.LoadProduces).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="保存", width=8, command=self.SaveProduces).pack(side="left", padx=2)
    
    def AddProduces(self):
        Value = self.ProducesEntry.get().strip()
        if Value:
            self.ProducesTable.insert("", tk.END, values=(Value,))
            self.ProducesEntry.delete(0, tk.END)
    
    def DeleteProduces(self):
        Selected = self.ProducesTable.selection()
        if Selected:
            self.ProducesTable.delete(Selected[0])
    
    def LoadProduces(self):
        Selected = self.ProducesTable.selection()
        if Selected:
            Values = self.ProducesTable.item(Selected[0], "values")
            self.ProducesEntry.delete(0, tk.END)
            if Values:
                self.ProducesEntry.insert(0, Values[0])
    
    def SaveProduces(self):
        Selected = self.ProducesTable.selection()
        Value = self.ProducesEntry.get().strip()
        if not Selected:
            self.AddProduces()
        elif Value:
            self.ProducesTable.item(Selected[0], values=(Value,))
            self.ProducesEntry.delete(0, tk.END)
    
    def CreateCanCarryGroup(self, ParentFrame):
        """创建可搭载单位组"""
        GroupFrame = ttk.LabelFrame(ParentFrame, text="允许搭载的单位")
        GroupFrame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(GroupFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(InputFrame, text="单位:").pack(side="left", padx=2)
        self.CanCarryEntry = ttk.Combobox(InputFrame, values=self.DB.Get("Units"), width=22)
        self.CanCarryEntry.pack(side="left", padx=2)
        ttk.Button(InputFrame, text="+", width=3, command=self.AddCanCarry).pack(side="left", padx=2)
        ttk.Button(InputFrame, text="-", width=3, command=self.DeleteCanCarry).pack(side="left", padx=2)
        
        # 表格
        TableFrame = ttk.Frame(GroupFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.CanCarryTable = ttk.Treeview(TableFrame, columns=("Unit",), show="headings", height=8)
        self.CanCarryTable.heading("Unit", text="单位")
        self.CanCarryTable.column("Unit", width=200)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.CanCarryTable.yview)
        self.CanCarryTable.configure(yscrollcommand=Scrollbar.set)
        self.CanCarryTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        BtnFrame = ttk.Frame(GroupFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text="读取", width=8, command=self.LoadCanCarry).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="保存", width=8, command=self.SaveCanCarry).pack(side="left", padx=2)
    
    def AddCanCarry(self):
        Value = self.CanCarryEntry.get().strip()
        if Value:
            self.CanCarryTable.insert("", tk.END, values=(Value,))
            self.CanCarryEntry.delete(0, tk.END)
    
    def DeleteCanCarry(self):
        Selected = self.CanCarryTable.selection()
        if Selected:
            self.CanCarryTable.delete(Selected[0])
    
    def LoadCanCarry(self):
        Selected = self.CanCarryTable.selection()
        if Selected:
            Values = self.CanCarryTable.item(Selected[0], "values")
            self.CanCarryEntry.delete(0, tk.END)
            if Values:
                self.CanCarryEntry.insert(0, Values[0])
    
    def SaveCanCarry(self):
        Selected = self.CanCarryTable.selection()
        Value = self.CanCarryEntry.get().strip()
        if not Selected:
            self.AddCanCarry()
        elif Value:
            self.CanCarryTable.item(Selected[0], values=(Value,))
            self.CanCarryEntry.delete(0, tk.END)
    
    def CreateAirwayGroup(self, ParentFrame):
        """创建航线组"""
        GroupFrame = ttk.LabelFrame(ParentFrame, text="航线配置")
        GroupFrame.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(GroupFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(InputFrame, text="发射数:").grid(row=0, column=0, padx=2)
        self.AirwayLaunchEntry = ttk.Entry(InputFrame, width=8)
        self.AirwayLaunchEntry.grid(row=0, column=1, padx=2)
        ttk.Label(InputFrame, text="间隔:").grid(row=1, column=0, padx=2)
        self.AirwayTimeEntry = ttk.Entry(InputFrame, width=8)
        self.AirwayTimeEntry.grid(row=1, column=1, padx=2)
        ttk.Button(InputFrame, text="+", width=3, command=self.AddAirway).grid(row=0, column=2, padx=2)
        ttk.Button(InputFrame, text="-", width=3, command=self.DeleteAirway).grid(row=1, column=2, padx=2)
        
        # 表格
        TableFrame = ttk.Frame(GroupFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.AirwayTable = ttk.Treeview(TableFrame, columns=("Launch", "Time"), show="headings", height=18)
        self.AirwayTable.heading("Launch", text="发射数")
        self.AirwayTable.heading("Time", text="间隔")
        self.AirwayTable.column("Launch", width=80)
        self.AirwayTable.column("Time", width=80)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.AirwayTable.yview)
        self.AirwayTable.configure(yscrollcommand=Scrollbar.set)
        self.AirwayTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        BtnFrame = ttk.Frame(GroupFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text="读取", width=8, command=self.LoadAirway).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="保存", width=8, command=self.SaveAirway).pack(side="left", padx=2)
    
    def AddAirway(self):
        Launch = self.AirwayLaunchEntry.get().strip()
        Time = self.AirwayTimeEntry.get().strip()
        if Launch and Time:
            self.AirwayTable.insert("", tk.END, values=(Launch, Time))
            self.AirwayLaunchEntry.delete(0, tk.END)
            self.AirwayTimeEntry.delete(0, tk.END)
    
    def DeleteAirway(self):
        Selected = self.AirwayTable.selection()
        if Selected:
            self.AirwayTable.delete(Selected[0])
    
    def LoadAirway(self):
        Selected = self.AirwayTable.selection()
        if Selected:
            Values = self.AirwayTable.item(Selected[0], "values")
            self.AirwayLaunchEntry.delete(0, tk.END)
            self.AirwayTimeEntry.delete(0, tk.END)
            if Values:
                self.AirwayLaunchEntry.insert(0, Values[0])
                if len(Values) > 1:
                    self.AirwayTimeEntry.insert(0, Values[1])
    
    def SaveAirway(self):
        Selected = self.AirwayTable.selection()
        Launch = self.AirwayLaunchEntry.get().strip()
        Time = self.AirwayTimeEntry.get().strip()
        if not Selected:
            self.AddAirway()
        elif Launch and Time:
            self.AirwayTable.item(Selected[0], values=(Launch, Time))
            self.AirwayLaunchEntry.delete(0, tk.END)
            self.AirwayTimeEntry.delete(0, tk.END)
    
    def CreateCanHostAircraftsGroup(self, ParentFrame):
        """创建子单位组"""
        GroupFrame = ttk.LabelFrame(ParentFrame, text="子单位配置")
        GroupFrame.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(GroupFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(InputFrame, text="单位名称:").grid(row=0, column=0, padx=2, sticky="w")
        self.HostUnitEntry = ttk.Combobox(InputFrame, values=self.DB.Get("Units"), width=17)
        self.HostUnitEntry.grid(row=0, column=1, columnspan=2, padx=2)
        
        ttk.Label(InputFrame, text="数量:").grid(row=0, column=3, padx=2)
        self.HostCountEntry = ttk.Entry(InputFrame, width=6)
        self.HostCountEntry.grid(row=0, column=4, padx=2)
        
        ttk.Label(InputFrame, text="航线:").grid(row=1, column=0, padx=2, sticky="w")
        self.HostAirwayEntry = ttk.Entry(InputFrame, width=6)
        self.HostAirwayEntry.grid(row=1, column=1, padx=2)
        
        ttk.Label(InputFrame, text="巡逻:").grid(row=1, column=2, padx=2)
        self.HostPatrolEntry = ttk.Entry(InputFrame, width=6)
        self.HostPatrolEntry.grid(row=1, column=3, padx=2)
        
        self.HostAutoPatrolVar = tk.BooleanVar()
        ttk.Checkbutton(InputFrame, text="自动巡逻", variable=self.HostAutoPatrolVar).grid(row=1, column=4, padx=2)
        
        BtnInputFrame = ttk.Frame(InputFrame)
        BtnInputFrame.grid(row=0, column=5, rowspan=2, padx=5)
        ttk.Button(BtnInputFrame, text="+", width=3, command=self.AddHostAircraft).pack(pady=2)
        ttk.Button(BtnInputFrame, text="-", width=3, command=self.DeleteHostAircraft).pack(pady=2)
        
        # 表格
        TableFrame = ttk.Frame(GroupFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        Columns = ("Unit", "Count", "Airway", "Patrol", "AutoPatrol")
        self.HostTable = ttk.Treeview(TableFrame, columns=Columns, show="headings", height=16)
        self.HostTable.heading("Unit", text="单位")
        self.HostTable.heading("Count", text="数量")
        self.HostTable.heading("Airway", text="航线")
        self.HostTable.heading("Patrol", text="巡逻")
        self.HostTable.heading("AutoPatrol", text="自巡逻")
        self.HostTable.column("Unit", width=150)
        self.HostTable.column("Count", width=50)
        self.HostTable.column("Airway", width=50)
        self.HostTable.column("Patrol", width=50)
        self.HostTable.column("AutoPatrol", width=50)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.HostTable.yview)
        self.HostTable.configure(yscrollcommand=Scrollbar.set)
        self.HostTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        BtnFrame = ttk.Frame(GroupFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text="读取", width=8, command=self.LoadHostAircraft).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="保存", width=8, command=self.SaveHostAircraft).pack(side="left", padx=2)
    
    def AddHostAircraft(self):
        Unit = self.HostUnitEntry.get().strip()
        Count = self.HostCountEntry.get().strip()
        if Unit and Count:
            Airway = self.HostAirwayEntry.get().strip()
            Patrol = self.HostPatrolEntry.get().strip()
            AutoPatrol = "√" if self.HostAutoPatrolVar.get() else ""
            self.HostTable.insert("", tk.END, values=(Unit, Count, Airway, Patrol, AutoPatrol))
            self.ClearHostInputs()
    
    def DeleteHostAircraft(self):
        Selected = self.HostTable.selection()
        if Selected:
            self.HostTable.delete(Selected[0])
    
    def LoadHostAircraft(self):
        Selected = self.HostTable.selection()
        if Selected:
            Values = self.HostTable.item(Selected[0], "values")
            self.ClearHostInputs()
            if Values:
                self.HostUnitEntry.insert(0, Values[0] if len(Values) > 0 else "")
                self.HostCountEntry.insert(0, Values[1] if len(Values) > 1 else "")
                self.HostAirwayEntry.insert(0, Values[2] if len(Values) > 2 else "")
                self.HostPatrolEntry.insert(0, Values[3] if len(Values) > 3 else "")
                self.HostAutoPatrolVar.set(Values[4] == "√" if len(Values) > 4 else False)
    
    def SaveHostAircraft(self):
        Selected = self.HostTable.selection()
        Unit = self.HostUnitEntry.get().strip()
        Count = self.HostCountEntry.get().strip()
        if not Selected:
            self.AddHostAircraft()
        elif Unit and Count:
            Airway = self.HostAirwayEntry.get().strip()
            Patrol = self.HostPatrolEntry.get().strip()
            AutoPatrol = "√" if self.HostAutoPatrolVar.get() else ""
            self.HostTable.item(Selected[0], values=(Unit, Count, Airway, Patrol, AutoPatrol))
            self.ClearHostInputs()
    
    def ClearHostInputs(self):
        self.HostUnitEntry.delete(0, tk.END)
        self.HostCountEntry.delete(0, tk.END)
        self.HostAirwayEntry.delete(0, tk.END)
        self.HostPatrolEntry.delete(0, tk.END)
        self.HostAutoPatrolVar.set(False)
    
    def CreateWeaponTab(self):
        """创建武器配置标签页"""
        Frame = ttk.Frame(self.Notebook)
        self.Notebook.add(Frame, text=self.Lang.Get("Tab_Weapon"))
        
        Frame.columnconfigure(0, weight=1)
        Frame.columnconfigure(1, weight=1)
        Frame.rowconfigure(0, weight=1)
        Frame.rowconfigure(1, weight=1)
        
        # 左侧：武器配置表格
        ConfigFrame = ttk.LabelFrame(Frame, text="武器配置")
        ConfigFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # 配置输入区
        ConfigInputFrame = ttk.Frame(ConfigFrame)
        ConfigInputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(ConfigInputFrame, text="配置名称:").pack(side="left", padx=2)
        self.ConfigNameEntry = ttk.Entry(ConfigInputFrame, width=20)
        self.ConfigNameEntry.pack(side="left", padx=2)
        ttk.Button(ConfigInputFrame, text="+", width=3, command=self.AddConfig).pack(side="left", padx=2)
        ttk.Button(ConfigInputFrame, text="-", width=3, command=self.DeleteConfig).pack(side="left", padx=2)
        
        # 配置表格
        ConfigTableFrame = ttk.Frame(ConfigFrame)
        ConfigTableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.ConfigTable = ttk.Treeview(ConfigTableFrame, columns=("Name", "Default", "OnlyFull"), show="headings", height=12)
        self.ConfigTable.heading("Name", text="配置名称")
        self.ConfigTable.heading("Default", text="Default")
        self.ConfigTable.heading("OnlyFull", text="OnlyFull")
        self.ConfigTable.column("Name", width=150)
        self.ConfigTable.column("Default", width=60)
        self.ConfigTable.column("OnlyFull", width=80)
        ConfigScrollbar = ttk.Scrollbar(ConfigTableFrame, orient="vertical", command=self.ConfigTable.yview)
        self.ConfigTable.configure(yscrollcommand=ConfigScrollbar.set)
        self.ConfigTable.pack(side="left", fill="both", expand=True)
        ConfigScrollbar.pack(side="right", fill="y")
        self.ConfigTable.bind("<<TreeviewSelect>>", self.OnConfigSelect)
        
        # 初始化时添加"无配置"选项
        self.ConfigTable.insert("", tk.END, values=("无配置", "", ""))
        
        # 配置选项区域
        self.ConfigOptionsFrame = ttk.Frame(ConfigFrame)
        self.ConfigDefaultVar = tk.BooleanVar()
        self.ConfigOnlyFullVar = tk.BooleanVar()
        
        ttk.Checkbutton(self.ConfigOptionsFrame, text="Default", variable=self.ConfigDefaultVar).pack(side="left", padx=5)
        ttk.Checkbutton(self.ConfigOptionsFrame, text="OnlyFull", variable=self.ConfigOnlyFullVar).pack(side="left", padx=5)
        
        # 配置按钮
        ConfigBtnFrame = ttk.Frame(ConfigFrame)
        ConfigBtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(ConfigBtnFrame, text="读取", width=8, command=self.LoadConfig).pack(side="left", padx=2)
        ttk.Button(ConfigBtnFrame, text="保存", width=8, command=self.SaveConfig).pack(side="left", padx=2)
        
        # 右侧：武器表格
        WeaponFrame = ttk.LabelFrame(Frame, text="武器")
        WeaponFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        # 武器输入区
        WeaponInputFrame = ttk.Frame(WeaponFrame)
        WeaponInputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(WeaponInputFrame, text="名称:").grid(row=0, column=0, padx=2, sticky="w")
        self.WeaponNameEntry = ttk.Combobox(WeaponInputFrame, values=self.DB.Get("Weapons"), width=15)
        self.WeaponNameEntry.grid(row=0, column=1, padx=2)
        
        ttk.Label(WeaponInputFrame, text="数量:").grid(row=0, column=2, padx=2)
        self.WeaponCountEntry = ttk.Entry(WeaponInputFrame, width=8)
        self.WeaponCountEntry.grid(row=0, column=3, padx=2)
        
        ttk.Label(WeaponInputFrame, text="Launch:").grid(row=1, column=0, padx=2, sticky="w")
        self.WeaponLaunchEntry = ttk.Entry(WeaponInputFrame, width=8)
        self.WeaponLaunchEntry.grid(row=1, column=1, padx=2)
        
        ttk.Label(WeaponInputFrame, text="Time:").grid(row=1, column=2, padx=2)
        self.WeaponTimeEntry = ttk.Entry(WeaponInputFrame, width=8)
        self.WeaponTimeEntry.grid(row=1, column=3, padx=2)
        
        ttk.Button(WeaponInputFrame, text="+", width=3, command=self.AddWeapon).grid(row=0, column=4, padx=2)
        ttk.Button(WeaponInputFrame, text="-", width=3, command=self.DeleteWeapon).grid(row=1, column=4, padx=2)
        
        # 武器选项
        WeaponOptionsFrame = ttk.Frame(WeaponInputFrame)
        WeaponOptionsFrame.grid(row=0, column=5, rowspan=2, padx=10)
        
        self.WeaponAutoEngageVar = tk.BooleanVar()
        self.WeaponPrincipalVar = tk.BooleanVar()
        self.WeaponDefaultOffVar = tk.BooleanVar()
        
        ttk.Checkbutton(WeaponOptionsFrame, text="AutoEngage", variable=self.WeaponAutoEngageVar).pack(anchor="w", pady=1)
        ttk.Checkbutton(WeaponOptionsFrame, text="Principal", variable=self.WeaponPrincipalVar).pack(anchor="w", pady=1)
        ttk.Checkbutton(WeaponOptionsFrame, text="DefaultOff", variable=self.WeaponDefaultOffVar).pack(anchor="w", pady=1)
        
        # 武器表格
        WeaponTableFrame = ttk.Frame(WeaponFrame)
        WeaponTableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.WeaponTable = ttk.Treeview(
            WeaponTableFrame, 
            columns=("Name", "Count", "Launch", "Time", "AutoEngage", "Principal", "DefaultOff"), 
            show="headings", 
            height=16
        )
        self.WeaponTable.heading("Name", text="名称")
        self.WeaponTable.heading("Count", text="数量")
        self.WeaponTable.heading("Launch", text="Launch")
        self.WeaponTable.heading("Time", text="Time")
        self.WeaponTable.heading("AutoEngage", text="AutoEngage")
        self.WeaponTable.heading("Principal", text="Principal")
        self.WeaponTable.heading("DefaultOff", text="DefaultOff")
        self.WeaponTable.column("Name", width=120)
        self.WeaponTable.column("Count", width=50)
        self.WeaponTable.column("Launch", width=50)
        self.WeaponTable.column("Time", width=50)
        self.WeaponTable.column("AutoEngage", width=70)
        self.WeaponTable.column("Principal", width=60)
        self.WeaponTable.column("DefaultOff", width=70)
        WeaponScrollbar = ttk.Scrollbar(WeaponTableFrame, orient="vertical", command=self.WeaponTable.yview)
        self.WeaponTable.configure(yscrollcommand=WeaponScrollbar.set)
        self.WeaponTable.pack(side="left", fill="both", expand=True)
        WeaponScrollbar.pack(side="right", fill="y")
        self.WeaponTable.bind("<<TreeviewSelect>>", self.OnWeaponSelect)
        
        # 武器按钮
        WeaponBtnFrame = ttk.Frame(WeaponFrame)
        WeaponBtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(WeaponBtnFrame, text="↑", width=3, command=self.MoveWeaponUp).pack(side="left", padx=2)
        ttk.Button(WeaponBtnFrame, text="↓", width=3, command=self.MoveWeaponDown).pack(side="left", padx=2)
        ttk.Button(WeaponBtnFrame, text="读取", width=8, command=self.LoadWeapon).pack(side="left", padx=2)
        ttk.Button(WeaponBtnFrame, text="保存", width=8, command=self.SaveWeapon).pack(side="left", padx=2)
        
        # 底部：配置-武器关联
        AssociationFrame = ttk.LabelFrame(Frame, text="配置-武器关联")
        AssociationFrame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        # 关联输入区
        AssocInputFrame = ttk.Frame(AssociationFrame)
        AssocInputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(AssocInputFrame, text="配置:").pack(side="left", padx=2)
        self.AssocConfigCombo = ttk.Combobox(AssocInputFrame, values=[], width=20, state="readonly")
        self.AssocConfigCombo.pack(side="left", padx=2)
        
        ttk.Label(AssocInputFrame, text="武器:").pack(side="left", padx=10)
        self.AssocWeaponCombo = ttk.Combobox(AssocInputFrame, values=[], width=20, state="readonly")
        self.AssocWeaponCombo.pack(side="left", padx=2)
        
        ttk.Button(AssocInputFrame, text="添加关联", command=self.AddWeaponConfigAssociation).pack(side="left", padx=10)
        
        # 关联表格
        AssocTableFrame = ttk.Frame(AssociationFrame)
        AssocTableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.WeaponConfigTable = ttk.Treeview(AssocTableFrame, columns=("Config", "Weapon"), show="headings", height=8)
        self.WeaponConfigTable.heading("Config", text="配置")
        self.WeaponConfigTable.heading("Weapon", text="武器")
        self.WeaponConfigTable.column("Config", width=200)
        self.WeaponConfigTable.column("Weapon", width=200)
        AssocScrollbar = ttk.Scrollbar(AssocTableFrame, orient="vertical", command=self.WeaponConfigTable.yview)
        self.WeaponConfigTable.configure(yscrollcommand=AssocScrollbar.set)
        self.WeaponConfigTable.pack(side="left", fill="both", expand=True)
        AssocScrollbar.pack(side="right", fill="y")
        
        # 关联表格按钮
        AssocBtnFrame = ttk.Frame(AssociationFrame)
        AssocBtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(AssocBtnFrame, text="↑", width=3, command=self.MoveAssocUp).pack(side="left", padx=2)
        ttk.Button(AssocBtnFrame, text="↓", width=3, command=self.MoveAssocDown).pack(side="left", padx=2)
        ttk.Button(AssocBtnFrame, text="删除关联", width=10, command=self.DeleteWeaponConfigAssociation).pack(side="left", padx=2)
        ttk.Button(AssocBtnFrame, text="清除所有", width=10, command=self.ClearAllAssociations).pack(side="left", padx=2)
        ttk.Button(AssocBtnFrame, text="读取", width=8, command=self.LoadAssociation).pack(side="left", padx=2)
        ttk.Button(AssocBtnFrame, text="保存", width=8, command=self.SaveAssociation).pack(side="left", padx=2)
        
        # 存储数据
        self.ConfigData = {}
        self.WeaponData = {}
        self.WeaponConfigAssociations = []
        
        # 更新关联下拉框
        self.UpdateAssociationComboboxes()
    
    def UpdateAssociationComboboxes(self):
        """更新关联下拉框"""
        # 更新配置下拉框
        ConfigNames = []
        for Item in self.ConfigTable.get_children():
            Values = self.ConfigTable.item(Item, "values")
            if Values and Values[0] != "无配置":
                ConfigNames.append(Values[0])
        self.AssocConfigCombo['values'] = ConfigNames
        
        # 更新武器下拉框
        WeaponNames = []
        for Item in self.WeaponTable.get_children():
            Values = self.WeaponTable.item(Item, "values")
            if Values and Values[0]:
                WeaponNames.append(Values[0])
        self.AssocWeaponCombo['values'] = WeaponNames
    
    def AddConfig(self):
        """添加武器配置"""
        Name = self.ConfigNameEntry.get().strip()
        if Name and Name not in self.ConfigData:
            # 检查是否已存在
            for Item in self.ConfigTable.get_children():
                if self.ConfigTable.item(Item, "values")[0] == Name:
                    return
            self.ConfigTable.insert("", tk.END, values=(Name, "", ""))
            self.ConfigData[Name] = {"Default": False, "OnlyFull": False}
            self.ConfigNameEntry.delete(0, tk.END)
            self.UpdateAssociationComboboxes()
    
    def DeleteConfig(self):
        """删除武器配置"""
        Selected = self.ConfigTable.selection()
        if Selected:
            Values = self.ConfigTable.item(Selected[0], "values")
            if Values and Values[0] != "无配置":
                ConfigName = Values[0]
                if ConfigName in self.ConfigData:
                    del self.ConfigData[ConfigName]
                self.ConfigTable.delete(Selected[0])
                self.UpdateAssociationComboboxes()
    
    def OnConfigSelect(self, Event=None):
        """配置选择事件"""
        Selected = self.ConfigTable.selection()
        if Selected:
            Values = self.ConfigTable.item(Selected[0], "values")
            if Values:
                ConfigName = Values[0]
                if ConfigName in self.ConfigData:
                    Data = self.ConfigData[ConfigName]
                    # 更新复选框状态已在LoadConfig中处理
                self.LoadConfig()
    
    def LoadConfig(self):
        """读取选中的配置"""
        Selected = self.ConfigTable.selection()
        if Selected:
            Values = self.ConfigTable.item(Selected[0], "values")
            if Values and Values[0] != "无配置":
                ConfigName = Values[0]
                self.ConfigNameEntry.delete(0, tk.END)
                self.ConfigNameEntry.insert(0, ConfigName)
                # 读取复选框状态
                DefaultChecked = Values[1] == "√"
                OnlyFullChecked = Values[2] == "√"
                # 更新复选框状态显示
                self.ConfigDefaultVar.set(DefaultChecked)
                self.ConfigOnlyFullVar.set(OnlyFullChecked)
                self.ConfigData[ConfigName]["Default"] = DefaultChecked
                self.ConfigData[ConfigName]["OnlyFull"] = OnlyFullChecked
                # 显示复选框区域
                self.ConfigOptionsFrame.pack(fill="x", padx=5, pady=5)
    
    def SaveConfig(self):
        """保存到选中的配置"""
        Selected = self.ConfigTable.selection()
        Name = self.ConfigNameEntry.get().strip()
        if not Selected:
            self.AddConfig()
        elif Name:
            OldValues = self.ConfigTable.item(Selected[0], "values")
            if OldValues and OldValues[0] != "无配置":
                OldName = OldValues[0]
                # 如果名称改变，更新数据
                if Name != OldName and Name in self.ConfigData:
                    # 名称已存在，不允许重复
                    return
                if OldName in self.ConfigData:
                    del self.ConfigData[OldName]
                
                # 获取当前复选框状态
                DefaultChecked = self.ConfigDefaultVar.get()
                OnlyFullChecked = self.ConfigOnlyFullVar.get()
                self.ConfigData[Name] = {"Default": DefaultChecked, "OnlyFull": OnlyFullChecked}
                
                # 更新表格显示
                DefaultStr = "√" if DefaultChecked else ""
                OnlyFullStr = "√" if OnlyFullChecked else ""
                self.ConfigTable.item(Selected[0], values=(Name, DefaultStr, OnlyFullStr))
                self.ConfigNameEntry.delete(0, tk.END)
                self.UpdateAssociationComboboxes()
    
    def AddWeapon(self):
        """添加武器"""
        Name = self.WeaponNameEntry.get().strip()
        Count = self.WeaponCountEntry.get().strip()
        if Name and Count:
            Launch = self.WeaponLaunchEntry.get().strip()
            Time = self.WeaponTimeEntry.get().strip()
            AutoEngage = "√" if self.WeaponAutoEngageVar.get() else ""
            Principal = "√" if self.WeaponPrincipalVar.get() else ""
            DefaultOff = "√" if self.WeaponDefaultOffVar.get() else ""
            
            self.WeaponTable.insert("", tk.END, values=(Name, Count, Launch, Time, AutoEngage, Principal, DefaultOff))
            self.WeaponData[Name] = {
                "Count": Count, "Launch": Launch, "Time": Time,
                "AutoEngage": AutoEngage, "Principal": Principal, "DefaultOff": DefaultOff
            }
            self.ClearWeaponInputs()
            self.UpdateAssociationComboboxes()
    
    def DeleteWeapon(self):
        """删除武器"""
        Selected = self.WeaponTable.selection()
        if Selected:
            Values = self.WeaponTable.item(Selected[0], "values")
            if Values and Values[0] in self.WeaponData:
                del self.WeaponData[Values[0]]
            self.WeaponTable.delete(Selected[0])
            self.ClearWeaponInputs()
            self.UpdateAssociationComboboxes()
    
    def ClearWeaponInputs(self):
        """清除武器输入"""
        self.WeaponNameEntry.delete(0, tk.END)
        self.WeaponCountEntry.delete(0, tk.END)
        self.WeaponLaunchEntry.delete(0, tk.END)
        self.WeaponTimeEntry.delete(0, tk.END)
        self.WeaponAutoEngageVar.set(False)
        self.WeaponPrincipalVar.set(False)
        self.WeaponDefaultOffVar.set(False)
    
    def OnWeaponSelect(self, Event=None):
        """武器选择事件"""
        self.LoadWeapon()
    
    def LoadWeapon(self):
        """读取选中的武器"""
        Selected = self.WeaponTable.selection()
        if Selected:
            Values = self.WeaponTable.item(Selected[0], "values")
            if Values:
                self.ClearWeaponInputs()
                if len(Values) > 0:
                    self.WeaponNameEntry.insert(0, Values[0])
                if len(Values) > 1:
                    self.WeaponCountEntry.insert(0, Values[1])
                if len(Values) > 2:
                    self.WeaponLaunchEntry.insert(0, Values[2])
                if len(Values) > 3:
                    self.WeaponTimeEntry.insert(0, Values[3])
                if len(Values) > 4:
                    self.WeaponAutoEngageVar.set(Values[4] == "√")
                if len(Values) > 5:
                    self.WeaponPrincipalVar.set(Values[5] == "√")
                if len(Values) > 6:
                    self.WeaponDefaultOffVar.set(Values[6] == "√")
    
    def SaveWeapon(self):
        """保存到选中的武器"""
        Selected = self.WeaponTable.selection()
        if not Selected:
            self.AddWeapon()
        else:
            Name = self.WeaponNameEntry.get().strip()
            Count = self.WeaponCountEntry.get().strip()
            if Name and Count:
                Launch = self.WeaponLaunchEntry.get().strip()
                Time = self.WeaponTimeEntry.get().strip()
                AutoEngage = "√" if self.WeaponAutoEngageVar.get() else ""
                Principal = "√" if self.WeaponPrincipalVar.get() else ""
                DefaultOff = "√" if self.WeaponDefaultOffVar.get() else ""
                
                self.WeaponTable.item(Selected[0], values=(Name, Count, Launch, Time, AutoEngage, Principal, DefaultOff))
                self.WeaponData[Name] = {
                    "Count": Count, "Launch": Launch, "Time": Time,
                    "AutoEngage": AutoEngage, "Principal": Principal, "DefaultOff": DefaultOff
                }
                self.ClearWeaponInputs()
                self.UpdateAssociationComboboxes()
    
    def MoveWeaponUp(self):
        """向上移动武器"""
        Selected = self.WeaponTable.selection()
        if Selected:
            Index = self.WeaponTable.index(Selected[0])
            if Index > 0:
                self.WeaponTable.move(Selected[0], "", Index - 1)
    
    def MoveWeaponDown(self):
        """向下移动武器"""
        Selected = self.WeaponTable.selection()
        if Selected:
            Index = self.WeaponTable.index(Selected[0])
            if Index < len(self.WeaponTable.get_children()) - 1:
                self.WeaponTable.move(Selected[0], "", Index + 1)
    
    def AddWeaponConfigAssociation(self):
        """添加武器配置关联"""
        ConfigName = self.AssocConfigCombo.get()
        WeaponName = self.AssocWeaponCombo.get()
        if ConfigName and WeaponName:
            # 检查是否已存在
            for Item in self.WeaponConfigTable.get_children():
                Values = self.WeaponConfigTable.item(Item, "values")
                if Values and Values[0] == ConfigName and Values[1] == WeaponName:
                    return
            self.WeaponConfigTable.insert("", tk.END, values=(ConfigName, WeaponName))
            self.WeaponConfigAssociations.append((ConfigName, WeaponName))
    
    def DeleteWeaponConfigAssociation(self):
        """删除武器配置关联"""
        Selected = self.WeaponConfigTable.selection()
        if Selected:
            Values = self.WeaponConfigTable.item(Selected[0], "values")
            if Values:
                ConfigName, WeaponName = Values[0], Values[1]
                self.WeaponConfigTable.delete(Selected[0])
                self.WeaponConfigAssociations = [
                    assoc for assoc in self.WeaponConfigAssociations 
                    if assoc != (ConfigName, WeaponName)
                ]
    
    def MoveAssocUp(self):
        """向上移动关联"""
        Selected = self.WeaponConfigTable.selection()
        if Selected:
            Index = self.WeaponConfigTable.index(Selected[0])
            if Index > 0:
                self.WeaponConfigTable.move(Selected[0], "", Index - 1)
    
    def MoveAssocDown(self):
        """向下移动关联"""
        Selected = self.WeaponConfigTable.selection()
        if Selected:
            Index = self.WeaponConfigTable.index(Selected[0])
            if Index < len(self.WeaponConfigTable.get_children()) - 1:
                self.WeaponConfigTable.move(Selected[0], "", Index + 1)
    
    def ClearAllAssociations(self):
        """清除所有关联"""
        if messagebox.askyesno(self.Lang.Get("Msg_Warning"), "确定要清除所有关联吗？"):
            for Item in self.WeaponConfigTable.get_children():
                self.WeaponConfigTable.delete(Item)
            self.WeaponConfigAssociations.clear()
    
    def LoadAssociation(self):
        """读取选中的关联"""
        Selected = self.WeaponConfigTable.selection()
        if Selected:
            Values = self.WeaponConfigTable.item(Selected[0], "values")
            if Values and len(Values) >= 2:
                self.AssocConfigCombo.set(Values[0])
                self.AssocWeaponCombo.set(Values[1])
    
    def SaveAssociation(self):
        """保存到选中的关联"""
        Selected = self.WeaponConfigTable.selection()
        if not Selected:
            self.AddWeaponConfigAssociation()
        else:
            ConfigName = self.AssocConfigCombo.get()
            WeaponName = self.AssocWeaponCombo.get()
            if ConfigName and WeaponName:
                self.WeaponConfigTable.item(Selected[0], values=(ConfigName, WeaponName))
                # 更新关联列表
                OldValues = self.WeaponConfigTable.item(Selected[0], "values")
                if OldValues:
                    OldConfigName, OldWeaponName = OldValues[0], OldValues[1]
                    self.WeaponConfigAssociations = [
                        assoc for assoc in self.WeaponConfigAssociations 
                        if assoc != (OldConfigName, OldWeaponName)
                    ]
                    self.WeaponConfigAssociations.append((ConfigName, WeaponName))
                self.AssocConfigCombo.set("")
                self.AssocWeaponCombo.set("")
    
    def CreateRadarModifierTab(self):
        """创建雷达/修改器标签页"""
        Frame = ttk.Frame(self.Notebook)
        self.Notebook.add(Frame, text=self.Lang.Get("Tab_RadarModifier"))
        
        Frame.columnconfigure(0, weight=1)
        Frame.columnconfigure(1, weight=1)
        Frame.rowconfigure(0, weight=1)
        
        # 雷达配置
        RadarFrame = ttk.LabelFrame(Frame, text="雷达配置")
        RadarFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        RadarInputFrame = ttk.Frame(RadarFrame)
        RadarInputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(RadarInputFrame, text="雷达名称:").pack(side="left", padx=2)
        self.RadarEntry = ttk.Combobox(RadarInputFrame, values=self.DB.Get("Radars"), width=30)
        self.RadarEntry.pack(side="left", padx=2)
        ttk.Button(RadarInputFrame, text="+", width=3, command=self.AddRadar).pack(side="left", padx=2)
        ttk.Button(RadarInputFrame, text="-", width=3, command=self.DeleteRadar).pack(side="left", padx=2)
        
        TableFrame = ttk.Frame(RadarFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.RadarTable = ttk.Treeview(TableFrame, columns=("Radar",), show="headings", height=20)
        self.RadarTable.heading("Radar", text="雷达名称")
        self.RadarTable.column("Radar", width=350)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.RadarTable.yview)
        self.RadarTable.configure(yscrollcommand=Scrollbar.set)
        self.RadarTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        BtnFrame = ttk.Frame(RadarFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text="读取", width=8, command=self.LoadRadar).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="保存", width=8, command=self.SaveRadar).pack(side="left", padx=2)
        
        # 修改器配置
        ModifierFrame = ttk.LabelFrame(Frame, text="修改器配置")
        ModifierFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        ModInputFrame = ttk.Frame(ModifierFrame)
        ModInputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(ModInputFrame, text="修改器:").grid(row=0, column=0, padx=2)
        self.ModifierNameEntry = ttk.Combobox(ModInputFrame, values=self.DB.Get("Modifiers"), width=25)
        self.ModifierNameEntry.grid(row=0, column=1, padx=2)
        ttk.Label(ModInputFrame, text="Value:").grid(row=1, column=0, padx=2)
        self.ModifierValueEntry = ttk.Entry(ModInputFrame, width=10)
        self.ModifierValueEntry.grid(row=1, column=1, padx=2, sticky="w")
        ttk.Button(ModInputFrame, text="+", width=3, command=self.AddModifier).grid(row=0, column=2, padx=2)
        ttk.Button(ModInputFrame, text="-", width=3, command=self.DeleteModifier).grid(row=1, column=2, padx=2)
        
        ModTableFrame = ttk.Frame(ModifierFrame)
        ModTableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.ModifierTable = ttk.Treeview(ModTableFrame, columns=("Name", "Value"), show="headings", height=18)
        self.ModifierTable.heading("Name", text="修改器名称")
        self.ModifierTable.heading("Value", text="Value")
        self.ModifierTable.column("Name", width=280)
        self.ModifierTable.column("Value", width=80)
        ModScrollbar = ttk.Scrollbar(ModTableFrame, orient="vertical", command=self.ModifierTable.yview)
        self.ModifierTable.configure(yscrollcommand=ModScrollbar.set)
        self.ModifierTable.pack(side="left", fill="both", expand=True)
        ModScrollbar.pack(side="right", fill="y")
        
        ModBtnFrame = ttk.Frame(ModifierFrame)
        ModBtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(ModBtnFrame, text="读取", width=8, command=self.LoadModifier).pack(side="left", padx=2)
        ttk.Button(ModBtnFrame, text="保存", width=8, command=self.SaveModifier).pack(side="left", padx=2)
    
    def AddRadar(self):
        Value = self.RadarEntry.get().strip()
        if Value:
            self.RadarTable.insert("", tk.END, values=(Value,))
            self.RadarEntry.delete(0, tk.END)
    
    def DeleteRadar(self):
        Selected = self.RadarTable.selection()
        if Selected:
            self.RadarTable.delete(Selected[0])
    
    def LoadRadar(self):
        Selected = self.RadarTable.selection()
        if Selected:
            Values = self.RadarTable.item(Selected[0], "values")
            self.RadarEntry.delete(0, tk.END)
            if Values:
                self.RadarEntry.insert(0, Values[0])
    
    def SaveRadar(self):
        Selected = self.RadarTable.selection()
        Value = self.RadarEntry.get().strip()
        if not Selected:
            self.AddRadar()
        elif Value:
            self.RadarTable.item(Selected[0], values=(Value,))
            self.RadarEntry.delete(0, tk.END)
    
    def AddModifier(self):
        Name = self.ModifierNameEntry.get().strip()
        if Name:
            Value = self.ModifierValueEntry.get().strip()
            self.ModifierTable.insert("", tk.END, values=(Name, Value))
            self.ModifierNameEntry.delete(0, tk.END)
            self.ModifierValueEntry.delete(0, tk.END)
    
    def DeleteModifier(self):
        Selected = self.ModifierTable.selection()
        if Selected:
            self.ModifierTable.delete(Selected[0])
    
    def LoadModifier(self):
        Selected = self.ModifierTable.selection()
        if Selected:
            Values = self.ModifierTable.item(Selected[0], "values")
            self.ModifierNameEntry.delete(0, tk.END)
            self.ModifierValueEntry.delete(0, tk.END)
            if Values:
                self.ModifierNameEntry.insert(0, Values[0])
                if len(Values) > 1 and Values[1]:
                    self.ModifierValueEntry.insert(0, Values[1])
    
    def SaveModifier(self):
        Selected = self.ModifierTable.selection()
        Name = self.ModifierNameEntry.get().strip()
        if not Selected:
            self.AddModifier()
        elif Name:
            Value = self.ModifierValueEntry.get().strip()
            self.ModifierTable.item(Selected[0], values=(Name, Value))
            self.ModifierNameEntry.delete(0, tk.END)
            self.ModifierValueEntry.delete(0, tk.END)
    
    def CreateStateSwitchTab(self):
        """创建状态切换标签页"""
        Frame = ttk.Frame(self.Notebook)
        self.Notebook.add(Frame, text=self.Lang.Get("Tab_StateSwitch"))
        
        Frame.columnconfigure(0, weight=1)
        Frame.columnconfigure(1, weight=1)
        Frame.rowconfigure(0, weight=1)
        
        # 状态设置组
        self.StateVars = {}
        StateFrame = ttk.LabelFrame(Frame, text="状态设置")
        StateFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # 特殊状态开关
        self.StateVars["SpecialState"] = tk.BooleanVar()
        ttk.Checkbutton(StateFrame, text="启用特殊状态 (SpecialState)", 
                        variable=self.StateVars["SpecialState"]).grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        # 状态名称
        StateFields = [
            ("HighState", "高状态名称:", 1),
            ("LowState", "低状态名称:", 2),
            ("TimeToHighState", "切换高状态时间:", 3),
            ("TimeToLowState", "切换低状态时间:", 4),
            ("HighStateStringIDX", "高状态字符串索引:", 5),
            ("LowStateStringIDX", "低状态字符串索引:", 6),
            ("StateStringIDX", "当前状态字符串索引:", 7),
            ("StateIcon", "状态图标路径:", 8),
            ("ToHighStateIcon", "切换高状态图标:", 9),
            ("ToLowStateIcon", "切换低状态图标:", 10),
            ("ToHighStateProcessingStringIDX", "高状态处理字符串:", 11),
            ("ToLowStateProcessingStringIDX", "低状态处理字符串:", 12),
            ("AutoOnRestDelay", "切换高状态延迟:", 13)
        ]
        
        for Key, Label, Row in StateFields:
            ttk.Label(StateFrame, text=Label).grid(row=Row, column=0, padx=10, pady=5, sticky="w")
            Var = tk.StringVar()
            self.StateVars[Key] = Var
            ttk.Entry(StateFrame, textvariable=Var, width=30).grid(row=Row, column=1, padx=10, pady=5, sticky="w")
        
        # 自动切换组
        AutoFrame = ttk.LabelFrame(Frame, text="自动切换设置")
        AutoFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # 切换选项：High/Low/None
        ShiftOptions = ["", "High", "Low", "None"]
        ShiftFields = [
            ("RetreatShift", "撤退状态:", 0),
            ("AttackShift", "攻击状态:", 1),
            ("DefenceShift", "防御状态:", 2),
            ("FastMoveShift", "快速移动状态:", 3),
            ("UnderIceShift", "冰下状态:", 4),
            ("AutoOnMove", "移动时自动切换:", 5),
            ("AutoOnRest", "待命时自动切换:", 6)
        ]
        
        for Key, Label, Row in ShiftFields:
            ttk.Label(AutoFrame, text=Label).grid(row=Row, column=0, padx=10, pady=8, sticky="w")
            Var = tk.StringVar()
            self.StateVars[Key] = Var
            Combo = ttk.Combobox(AutoFrame, textvariable=Var, values=ShiftOptions, width=15, state="readonly")
            Combo.grid(row=Row, column=1, padx=10, pady=8, sticky="w")
    
    def CreateUpgradeTab(self):
        """创建升级项标签页"""
        Frame = ttk.Frame(self.Notebook)
        self.Notebook.add(Frame, text=self.Lang.Get("Tab_Upgrade"))
        
        Frame.columnconfigure(0, weight=1)
        Frame.columnconfigure(1, weight=1)
        Frame.rowconfigure(0, weight=1)
        
        # 升级项组（新的ImprovedBy格式）
        UpgradeFrame = ttk.LabelFrame(Frame, text="升级项 (ImprovedBy)")
        UpgradeFrame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(UpgradeFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(InputFrame, text="科技名称:").grid(row=0, column=0, padx=2, sticky="w")
        self.UpgradeTechEntry = ttk.Combobox(InputFrame, values=self.DB.Get("Techs"), width=25)
        self.UpgradeTechEntry.grid(row=0, column=1, padx=2)
        
        # Set/Add复选框
        OptionsFrame = ttk.Frame(InputFrame)
        OptionsFrame.grid(row=0, column=2, padx=10)
        self.UpgradeSetVar = tk.BooleanVar()
        self.UpgradeAddVar = tk.BooleanVar()
        ttk.Checkbutton(OptionsFrame, text="Set (修改值)", variable=self.UpgradeSetVar).pack(anchor="w", pady=1)
        ttk.Checkbutton(OptionsFrame, text="Add (增加值)", variable=self.UpgradeAddVar).pack(anchor="w", pady=1)
        
        ttk.Label(InputFrame, text="升级项:").grid(row=1, column=0, padx=2, sticky="w")
        self.UpgradePropertyEntry = ttk.Entry(InputFrame, width=25)
        self.UpgradePropertyEntry.grid(row=1, column=1, padx=2)
        
        ttk.Label(InputFrame, text="数值:").grid(row=1, column=2, padx=2, sticky="w")
        self.UpgradeValueEntry = ttk.Entry(InputFrame, width=15)
        self.UpgradeValueEntry.grid(row=1, column=3, padx=2)
        
        BtnInputFrame = ttk.Frame(InputFrame)
        BtnInputFrame.grid(row=0, column=4, rowspan=2, padx=5)
        ttk.Button(BtnInputFrame, text="+", width=3, command=self.AddUpgrade).pack(pady=2)
        ttk.Button(BtnInputFrame, text="-", width=3, command=self.DeleteUpgrade).pack(pady=2)
        
        # 升级项表格
        TableFrame = ttk.Frame(UpgradeFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.UpgradeTable = ttk.Treeview(
            TableFrame, 
            columns=("Tech", "Set", "Add", "Property", "Value"), 
            show="headings", 
            height=20
        )
        self.UpgradeTable.heading("Tech", text="科技名称")
        self.UpgradeTable.heading("Set", text="Set")
        self.UpgradeTable.heading("Add", text="Add")
        self.UpgradeTable.heading("Property", text="升级项")
        self.UpgradeTable.heading("Value", text="数值")
        self.UpgradeTable.column("Tech", width=150)
        self.UpgradeTable.column("Set", width=50)
        self.UpgradeTable.column("Add", width=50)
        self.UpgradeTable.column("Property", width=150)
        self.UpgradeTable.column("Value", width=100)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.UpgradeTable.yview)
        self.UpgradeTable.configure(yscrollcommand=Scrollbar.set)
        self.UpgradeTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        # 按钮
        BtnFrame = ttk.Frame(UpgradeFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text="↑", width=3, command=self.MoveUpgradeUp).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="↓", width=3, command=self.MoveUpgradeDown).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="读取", width=8, command=self.LoadUpgrade).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text="保存", width=8, command=self.SaveUpgrade).pack(side="left", padx=2)
        
        # 存储升级项数据
        self.UpgradeData = {}
    
    def AddUpgrade(self):
        """添加升级项"""
        Tech = self.UpgradeTechEntry.get().strip()
        Property = self.UpgradePropertyEntry.get().strip()
        Value = self.UpgradeValueEntry.get().strip()
        
        if Tech and Property and Value:
            SetChecked = "√" if self.UpgradeSetVar.get() else ""
            AddChecked = "√" if self.UpgradeAddVar.get() else ""
            
            # 检查是否已存在
            for Item in self.UpgradeTable.get_children():
                Values = self.UpgradeTable.item(Item, "values")
                if Values and Values[0] == Tech and Values[3] == Property:
                    return
            
            self.UpgradeTable.insert("", tk.END, values=(Tech, SetChecked, AddChecked, Property, Value))
            self.UpgradeData[f"{Tech}_{Property}"] = {
                "Tech": Tech,
                "Set": self.UpgradeSetVar.get(),
                "Add": self.UpgradeAddVar.get(),
                "Property": Property,
                "Value": Value
            }
            self.ClearUpgradeInputs()
    
    def DeleteUpgrade(self):
        """删除选中的升级项"""
        Selected = self.UpgradeTable.selection()
        if Selected:
            Values = self.UpgradeTable.item(Selected[0], "values")
            if Values:
                Key = f"{Values[0]}_{Values[3]}"
                if Key in self.UpgradeData:
                    del self.UpgradeData[Key]
            self.UpgradeTable.delete(Selected[0])
    
    def LoadUpgrade(self):
        """读取选中的升级项"""
        Selected = self.UpgradeTable.selection()
        if Selected:
            Values = self.UpgradeTable.item(Selected[0], "values")
            if Values:
                self.ClearUpgradeInputs()
                self.UpgradeTechEntry.insert(0, Values[0])
                self.UpgradeSetVar.set(Values[1] == "√")
                self.UpgradeAddVar.set(Values[2] == "√")
                self.UpgradePropertyEntry.insert(0, Values[3])
                self.UpgradeValueEntry.insert(0, Values[4])
    
    def SaveUpgrade(self):
        """保存到选中的升级项"""
        Selected = self.UpgradeTable.selection()
        if not Selected:
            self.AddUpgrade()
        else:
            Tech = self.UpgradeTechEntry.get().strip()
            Property = self.UpgradePropertyEntry.get().strip()
            Value = self.UpgradeValueEntry.get().strip()
            
            if Tech and Property and Value:
                SetChecked = "√" if self.UpgradeSetVar.get() else ""
                AddChecked = "√" if self.UpgradeAddVar.get() else ""
                
                self.UpgradeTable.item(Selected[0], values=(Tech, SetChecked, AddChecked, Property, Value))
                self.UpgradeData[f"{Tech}_{Property}"] = {
                    "Tech": Tech,
                    "Set": self.UpgradeSetVar.get(),
                    "Add": self.UpgradeAddVar.get(),
                    "Property": Property,
                    "Value": Value
                }
                self.ClearUpgradeInputs()
    
    def MoveUpgradeUp(self):
        """向上移动升级项"""
        Selected = self.UpgradeTable.selection()
        if Selected:
            Index = self.UpgradeTable.index(Selected[0])
            if Index > 0:
                self.UpgradeTable.move(Selected[0], "", Index - 1)
    
    def MoveUpgradeDown(self):
        """向下移动升级项"""
        Selected = self.UpgradeTable.selection()
        if Selected:
            Index = self.UpgradeTable.index(Selected[0])
            if Index < len(self.UpgradeTable.get_children()) - 1:
                self.UpgradeTable.move(Selected[0], "", Index + 1)
    
    def ClearUpgradeInputs(self):
        """清除升级项输入"""
        self.UpgradeTechEntry.delete(0, tk.END)
        self.UpgradeSetVar.set(False)
        self.UpgradeAddVar.set(False)
        self.UpgradePropertyEntry.delete(0, tk.END)
        self.UpgradeValueEntry.delete(0, tk.END)
    
    def CreateBottomButtons(self):
        """创建底部按钮"""
        ButtonFrame = ttk.Frame(self.MainFrame)
        ButtonFrame.pack(side="bottom", anchor="se", padx=5, pady=5)
        
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Clear"),
                   command=self.ClearAll).pack(side="left", padx=5)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Default"),
                   command=self.FillDefault).pack(side="left", padx=5)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Generate"),
                   command=self.GenerateCode).pack(side="left", padx=5)
    
    def ClearAll(self):
        """清除所有数据"""
        if messagebox.askokcancel(self.Lang.Get("Msg_Warning"), 
                                   self.Lang.Get("Msg_ConfirmClear")):
            for Var in self.BasicInfoVars.values():
                Var.set("")
            for Item in self.CustomParamsTable.get_children():
                self.CustomParamsTable.delete(Item)
    
    def FillDefault(self):
        """填充默认值"""
        if messagebox.askokcancel(self.Lang.Get("Msg_Warning"),
                                   self.Lang.Get("Msg_ConfirmDefault")):
            self.ClearAll()
            # 填充默认值示例
            Defaults = {
                "GlobalName": "NameExample",
                "Tech": "U_TechExample",
                "Type": "Ground",
                "Class": "UC_Ground",
                "Movie": "Units/Images/[Type]/Topdown/Example.midx",
                "AbstractMovie": "Units/Images/[Type]/Abstract/Example.midx",
                "Model": "Units/Images/[Type]/Example.midx",
                "Icon": "Units/Images/Icons/[Type]/Example.png",
                "IconIDX": "52",
                "DrawSize": "25",
                "Power": "10",
                "Size": "0.5",
                "Speed": "60",
                "TurnSpeed": "30",
                "ProductionCost": "0.5"
            }
            for Key, Value in Defaults.items():
                if Key in self.BasicInfoVars:
                    self.BasicInfoVars[Key].set(Value)
    
    def GenerateCode(self):
        """生成代码"""
        # 检查必填字段
        Required = ["GlobalName", "Tech", "Type", "Movie", "Icon"]
        for Key in Required:
            if Key in self.BasicInfoVars and not self.BasicInfoVars[Key].get().strip():
                messagebox.showwarning(self.Lang.Get("Msg_Warning"),
                                        self.Lang.Get("Msg_RequiredFields"))
                return
        
        # 生成代码
        Code = self.BuildCodeString()
        
        # 显示结果窗口
        OutputWindow = tk.Toplevel(self.Root)
        OutputWindow.title("Generated Code")
        OutputWindow.geometry("700x800")
        
        # 顶部按钮栏
        BtnFrame = ttk.Frame(OutputWindow)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        
        def CopyToClipboard():
            OutputWindow.clipboard_clear()
            OutputWindow.clipboard_append(Code)
            messagebox.showinfo(self.Lang.Get("Msg_Success"), "代码已复制到剪贴板")
        
        def SaveToFile():
            FilePath = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if FilePath:
                with open(FilePath, "w", encoding="utf-8") as f:
                    f.write(Code)
                messagebox.showinfo(self.Lang.Get("Msg_Success"), f"代码已保存到 {FilePath}")
        
        ttk.Button(BtnFrame, text="复制代码", command=CopyToClipboard).pack(side="left", padx=5)
        ttk.Button(BtnFrame, text="保存到文件", command=SaveToFile).pack(side="left", padx=5)
        ttk.Button(BtnFrame, text="关闭", command=OutputWindow.destroy).pack(side="right", padx=5)
        
        # 文本区域
        TextFrame = ttk.Frame(OutputWindow)
        TextFrame.pack(fill="both", expand=True, padx=5, pady=5)
        
        Scrollbar = tk.Scrollbar(TextFrame, orient="vertical")
        Scrollbar.pack(side="right", fill="y")
        
        TextWidget = tk.Text(TextFrame, width=80, height=45, 
                             font=("Consolas", 10), yscrollcommand=Scrollbar.set)
        TextWidget.pack(side="left", fill="both", expand=True)
        Scrollbar.config(command=TextWidget.yview)
        
        TextWidget.insert(tk.END, Code)
    
    def BuildCodeString(self):
        """构建代码字符串"""
        Lines = []
        
        # 单位名称
        Name = self.BasicInfoVars.get("GlobalName", tk.StringVar()).get()
        if Name:
            Lines.append(f'[UNIT] "{Name}"')
        
        # 基础属性
        Lines.extend(self.BuildBasicInfoCode())
        
        # 行为控制
        Lines.extend(self.BuildBehaviorCode())
        
        # 雷达配置
        Lines.extend(self.BuildRadarCode())
        
        # 修改器配置
        Lines.extend(self.BuildModifierCode())
        
        # 生产单位
        Lines.extend(self.BuildProducesCode())
        
        # 搭载单位
        Lines.extend(self.BuildCanCarryCode())
        
        # 航线配置
        Lines.extend(self.BuildAirwayCode())
        
        # 子单位配置
        Lines.extend(self.BuildCanHostAircraftsCode())
        
        # 武器配置
        Lines.extend(self.BuildWeaponCode())
        
        # 状态切换
        Lines.extend(self.BuildStateCode())
        
        # 升级项
        Lines.extend(self.BuildUpgradeCode())
        
        # 自定义参数
        for Item in self.CustomParamsTable.get_children():
            Values = self.CustomParamsTable.item(Item, "values")
            if Values and len(Values) >= 2:
                Lines.append(f'    {Values[0]} {Values[1]}')
        
        return "\n".join(Lines)
    
    def BuildBasicInfoCode(self):
        """生成基础信息代码"""
        Lines = []
        FieldMap = [
            ("Tech", "Tech", True),
            ("Type", "Type", False),
            ("Class", "Class", False),
            ("Movie", "Movie", True),
            ("AbstractMovie", "AbstractMovie", True),
            ("Model", "Model", True),
            ("Icon", "Icon", True),
            ("RoundIcon", "RoundIcon", True),
            ("IconIDX", "IconIDX", False),
            ("DrawSize", "DrawSize", False),
            ("AbstractDrawSize", "AbstractDrawSize", False),
            ("Sound", "Sound", False),
            ("LaunchMeSound", "LaunchMeSound", False),
            ("LaunchMePathIcon", "LaunchMePathIcon", True),
            ("DrawOrder", "DrawOrder", False),
            ("Crash", "Crash", True),
            ("Power", "Power", False),
            ("Size", "Size", False),
            ("Speed", "Speed", False),
            ("TurnSpeed", "TurnSpeed", False),
            ("Range", "Range", False),
            ("ProductionCost", "ProductionCost", False),
            ("SelfDestruct", "SelfDestruct", False),
            ("MaxElevation", "MaxElevation", False),
            ("MinElevation", "MinElevation", False),
            ("AutoRepair", "AutoRepair", False),
            ("ResupplyRadius", "ResupplyRadius", False),
            ("FollowRadius", "FollowRadius", False),
            ("OccupationRadius", "OccupationRadius", False),
            ("MaxAutoEngageRange", "MaxAutoEngageRange", False),
            ("ProductionPlacementRadius", "ProductionPlacementRadius", False),
            ("MaxNumberOnMap", "MaxNumberOnMap", False),
            ("MaxNumberToOrder", "MaxNumberToOrder", False),
            ("HangarSpaceRequired", "HangarSpaceRequired", False),
            ("HangarMaxLoad", "HangarMaxLoad", False)
        ]
        
        for VarKey, OutputKey, Quoted in FieldMap:
            Value = self.BasicInfoVars.get(VarKey, tk.StringVar()).get()
            if Value:
                if Quoted:
                    Lines.append(f'    {OutputKey} "{Value}"')
                else:
                    Lines.append(f'    {OutputKey} {Value}')
        return Lines
    
    def BuildBehaviorCode(self):
        """生成行为控制代码"""
        Lines = []
        for VarName, Data in self.BehaviorVars.items():
            Var = Data["Var"]
            CodeKey = Data["CodeKey"]
            BType = Data["Type"]
            HideRule = Data["HideRule"]
            
            IsChecked = Var.get()
            
            if HideRule == "HideWhenFalse" and not IsChecked:
                continue
            
            if BType == "Boolean":
                Value = "Yes" if IsChecked else "No"
                Lines.append(f'    {CodeKey} {Value}')
            elif BType == "Existed" and IsChecked:
                Lines.append(f'    {CodeKey}')
        return Lines
    
    def BuildRadarCode(self):
        """生成雷达配置代码"""
        Lines = []
        Items = self.RadarTable.get_children()
        if Items:
            for Item in Items:
                Values = self.RadarTable.item(Item, "values")
                if Values and Values[0]:
                    Lines.append(f'    Radar "{Values[0]}"')
        return Lines
    
    def BuildModifierCode(self):
        """生成修改器配置代码"""
        Lines = []
        Items = self.ModifierTable.get_children()
        if Items:
            Lines.append('    Modifiers')
            Lines.append('    {')
            for Item in Items:
                Values = self.ModifierTable.item(Item, "values")
                if Values and Values[0]:
                    ModName = Values[0]
                    ModValue = Values[1] if len(Values) > 1 and Values[1] else ""
                    if ModValue:
                        Lines.append(f'        {ModName} {{ Value {ModValue} }}')
                    else:
                        Lines.append(f'        {ModName}')
            Lines.append('    }')
        return Lines
    
    def BuildProducesCode(self):
        """生成生产单位代码"""
        Lines = []
        Items = self.ProducesTable.get_children()
        if Items:
            Lines.append('    Produces')
            Lines.append('    {')
            for Item in Items:
                Values = self.ProducesTable.item(Item, "values")
                if Values and Values[0]:
                    Lines.append(f'        "{Values[0]}"')
            Lines.append('    }')
        return Lines
    
    def BuildCanCarryCode(self):
        """生成搭载单位代码"""
        Lines = []
        Items = self.CanCarryTable.get_children()
        if Items:
            Lines.append('    CanCarry')
            Lines.append('    {')
            for Item in Items:
                Values = self.CanCarryTable.item(Item, "values")
                if Values and Values[0]:
                    Lines.append(f'        "{Values[0]}"')
            Lines.append('    }')
        return Lines
    
    def BuildAirwayCode(self):
        """生成航线配置代码"""
        Lines = []
        Items = self.AirwayTable.get_children()
        if Items:
            Lines.append('    Airway')
            Lines.append('    {')
            for Item in Items:
                Values = self.AirwayTable.item(Item, "values")
                if Values and len(Values) >= 2:
                    Lines.append(f'        Launch {Values[0]} Time {Values[1]}')
            Lines.append('    }')
        return Lines
    
    def BuildCanHostAircraftsCode(self):
        """生成子单位配置代码"""
        Lines = []
        Items = self.HostTable.get_children()
        if Items:
            Lines.append('    CanHostAircrafts')
            Lines.append('    {')
            for Item in Items:
                Values = self.HostTable.item(Item, "values")
                if Values and len(Values) >= 2:
                    UnitName = Values[0]
                    Count = Values[1]
                    Airway = Values[2] if len(Values) > 2 and Values[2] else ""
                    Patrol = Values[3] if len(Values) > 3 and Values[3] else ""
                    AutoPatrol = Values[4] if len(Values) > 4 else ""
                    
                    SubLines = [f'Unit "{UnitName}"', f'Count {Count}']
                    if Airway:
                        SubLines.append(f'Airway {Airway}')
                    if Patrol:
                        SubLines.append(f'Patrol {Patrol}')
                    if AutoPatrol == "√":
                        SubLines.append('AutoPatrol Yes')
                    
                    Lines.append('        {')
                    for SubLine in SubLines:
                        Lines.append(f'            {SubLine}')
                    Lines.append('        }')
            Lines.append('    }')
        return Lines
    
    def BuildWeaponCode(self):
        """生成武器配置代码"""
        Lines = []
        
        # 按配置分组处理武器
        ConfigWeapons = {}
        
        # 首先处理关联表
        for Item in self.WeaponConfigTable.get_children():
            Values = self.WeaponConfigTable.item(Item, "values")
            if Values and len(Values) >= 2:
                ConfigName, WeaponName = Values[0], Values[1]
                if ConfigName not in ConfigWeapons:
                    ConfigWeapons[ConfigName] = []
                ConfigWeapons[ConfigName].append(WeaponName)
        
        # 处理"无配置"的武器
        UnconfigWeapons = []
        for Item in self.WeaponTable.get_children():
            Values = self.WeaponTable.item(Item, "values")
            if Values and Values[0]:
                WeaponName = Values[0]
                # 检查是否在关联表中
                IsAssociated = False
                for ConfigName in ConfigWeapons:
                    if WeaponName in ConfigWeapons[ConfigName]:
                        IsAssociated = True
                        break
                if not IsAssociated:
                    UnconfigWeapons.append(WeaponName)
        
        # 生成武器配置代码
        AllConfigs = set(ConfigWeapons.keys())
        
        # 处理有配置的武器
        for ConfigName in AllConfigs:
            Lines.append('    Weapons')
            Lines.append('    {')
            Lines.append(f'        Config "{ConfigName}"')
            
            # 添加Default和OnlyFull选项
            if ConfigName in self.ConfigData:
                ConfigInfo = self.ConfigData[ConfigName]
                if ConfigInfo.get("Default"):
                    Lines.append('            Default')
                if ConfigInfo.get("OnlyFull"):
                    Lines.append('            OnlyFull')
            
            # 添加该配置下的武器
            for WeaponName in ConfigWeapons[ConfigName]:
                if WeaponName in self.WeaponData:
                    WeaponInfo = self.WeaponData[WeaponName]
                    Lines.append(f'            Weapon "{WeaponName}" {WeaponInfo.get("Count", "1")}')
                    
                    # 添加可选参数
                    if WeaponInfo.get("Launch"):
                        Lines.append(f'                Launch {WeaponInfo["Launch"]}')
                    if WeaponInfo.get("Time"):
                        Lines.append(f'                Time {WeaponInfo["Time"]}')
                    if WeaponInfo.get("AutoEngage"):
                        Lines.append('                AutoEngage')
                    if WeaponInfo.get("Principal"):
                        Lines.append('                Principal')
                    if WeaponInfo.get("DefaultOff"):
                        Lines.append('                DefaultOff')
            
            Lines.append('    }')
        
        # 处理无配置的武器
        if UnconfigWeapons:
            Lines.append('    Weapons')
            Lines.append('    {')
            for WeaponName in UnconfigWeapons:
                if WeaponName in self.WeaponData:
                    WeaponInfo = self.WeaponData[WeaponName]
                    Lines.append(f'        Weapon "{WeaponName}" {WeaponInfo.get("Count", "1")}')
                    
                    # 添加可选参数
                    if WeaponInfo.get("Launch"):
                        Lines.append(f'            Launch {WeaponInfo["Launch"]}')
                    if WeaponInfo.get("Time"):
                        Lines.append(f'            Time {WeaponInfo["Time"]}')
                    if WeaponInfo.get("AutoEngage"):
                        Lines.append('            AutoEngage')
                    if WeaponInfo.get("Principal"):
                        Lines.append('            Principal')
                    if WeaponInfo.get("DefaultOff"):
                        Lines.append('            DefaultOff')
            Lines.append('    }')
        
        return Lines
    
    def BuildStateCode(self):
        """生成状态切换代码"""
        Lines = []
        
        # 检查是否启用特殊状态
        if not self.StateVars.get("SpecialState") or not self.StateVars["SpecialState"].get():
            return Lines
        
        Lines.append('    SpecialState Yes')
        
        # 状态名称字段
        StateFields = [
            ("HighState", "HighState", True),
            ("LowState", "LowState", True),
            ("TimeToHighState", "TimeToHighState", False),
            ("TimeToLowState", "TimeToLowState", False),
            ("HighStateStringIDX", "HighStateStringIDX", False),
            ("LowStateStringIDX", "LowStateStringIDX", False),
            ("StateStringIDX", "StateStringIDX", False),
            ("StateIcon", "StateIcon", True),
            ("ToHighStateIcon", "ToHighStateIcon", True),
            ("ToLowStateIcon", "ToLowStateIcon", True),
            ("ToHighStateProcessingStringIDX", "ToHighStateProcessingStringIDX", False),
            ("ToLowStateProcessingStringIDX", "ToLowStateProcessingStringIDX", False),
            ("AutoOnRestDelay", "AutoOnRestDelay", False)
        ]
        
        for VarKey, OutputKey, Quoted in StateFields:
            Var = self.StateVars.get(VarKey)
            if Var:
                Value = Var.get() if hasattr(Var, 'get') else ""
                if Value:
                    if Quoted:
                        Lines.append(f'    {OutputKey} "{Value}"')
                    else:
                        Lines.append(f'    {OutputKey} {Value}')
        
        # 自动切换设置
        ShiftFields = ["RetreatShift", "AttackShift", "DefenceShift", 
                      "FastMoveShift", "UnderIceShift", "AutoOnMove", "AutoOnRest"]
        for Field in ShiftFields:
            Var = self.StateVars.get(Field)
            if Var:
                Value = Var.get() if hasattr(Var, 'get') else ""
                if Value:
                    Lines.append(f'    {Field} {Value}')
        
        return Lines
    
    def BuildUpgradeCode(self):
        """生成升级项代码"""
        Lines = []
        
        # 新的ImprovedBy格式升级项
        Items = self.UpgradeTable.get_children()
        if Items:
            Lines.append('    ImprovedBy')
            Lines.append('    {')
            for Item in Items:
                Values = self.UpgradeTable.item(Item, "values")
                if Values and len(Values) >= 5:
                    Tech = Values[0]
                    SetChecked = Values[1] == "√"
                    AddChecked = Values[2] == "√"
                    Property = Values[3]
                    Value = Values[4]
                    
                    # 构建升级项代码
                    UpgradeLine = f'        "{Tech}"'
                    
                    # 添加Set或Add选项
                    if AddChecked:
                        UpgradeLine += f' Add {Property} {Value}'
                    elif SetChecked:
                        UpgradeLine += f' Set {Property} {Value}'
                    else:
                        # 如果都没有勾选，只输出科技名称
                        pass
                    
                    Lines.append(UpgradeLine)
            Lines.append('    }')
        
        return Lines
    
    def ImportConfig(self):
        """导入配置"""
        FilePath = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if FilePath:
            try:
                with open(FilePath, "r", encoding="utf-8") as f:
                    Data = json.load(f)
                # TODO: 解析并填充数据
                messagebox.showinfo(self.Lang.Get("Msg_Success"), "Configuration imported.")
            except Exception as e:
                messagebox.showerror(self.Lang.Get("Msg_Error"), str(e))
    
    def ExportConfig(self):
        """导出配置"""
        FilePath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if FilePath:
            try:
                Data = {
                    "BasicInfo": {k: v.get() for k, v in self.BasicInfoVars.items()},
                    "CustomParams": [
                        self.CustomParamsTable.item(Item, "values")
                        for Item in self.CustomParamsTable.get_children()
                    ]
                }
                with open(FilePath, "w", encoding="utf-8") as f:
                    json.dump(Data, f, ensure_ascii=False, indent=4)
                messagebox.showinfo(self.Lang.Get("Msg_Success"), "Configuration exported.")
            except Exception as e:
                messagebox.showerror(self.Lang.Get("Msg_Error"), str(e))
    
    def Run(self):
        """运行应用"""
        self.Root.mainloop()


# ============================================================================
# 程序入口
# ============================================================================

if __name__ == "__main__":
    App = UnitCodeGeneratorApp()
    App.Run()
