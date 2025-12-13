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
            "Group_AllowedProduction": "生产单位",
            "Group_AllowedCarry": "可搭载单位",
            "Group_UpgradeItems": "升级项 (ImprovedBy)",
            "Group_StateSettings": "状态设置",
            "Group_AutoShift": "自动切换设置",
            "Group_AirwayConfig": "航线配置",
            "Group_SubUnitConfig": "子单位配置",
            "Label_GlobalName": "全局名称:",
            "Label_Tech": "科技引用:",
            "Label_Type": "单位类型:",
            "Label_Class": "单位分组:",
            "Label_Movie": "俯视图路径:",
            "Label_AbstractMovie": "缩略图路径:",
            "Label_Model": "3D模型路径:",
            "Label_Icon": "图标路径:",
            "Label_RoundIcon": "圆形图标:",
            "Label_DrawSize": "绘制大小:",
            "Label_AbstractDrawSize": "缩略绘制:",
            "Label_ModelDrawSize": "模型尺寸:",
            "Label_Sound": "音效编码:",
            "Label_SoundVolume": "音效音量:",
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
            "Label_Unit": "单位",
            "Label_TechName": "科技名称:",
            "Label_UpgradeProperty": "升级项:",
            "Label_Value": "数值:",
            "Label_SetValue": "Set (修改值)",
            "Label_AddValue": "Add (增加值)",
            "Label_UnitName": "单位名称:",
            "Label_Count": "数量:",
            "Label_Airway": "航线:",
            "Label_Patrol": "巡逻:",
            "Label_AutoPatrol": "自动巡逻",
            "Label_ConfigName": "配置名称:",
            "Label_WeaponName": "武器名称:",
            "Label_LaunchCount": "发射数:",
            "Label_Interval": "间隔:",
            "Label_RadarName": "雷达名称:",
            "Label_Modifier": "修改器:",
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
            "Btn_CopyCode": "复制代码",
            "Btn_SaveToFile": "保存到文件",
            "Btn_Close": "关闭",
            "Col_Parameter": "参数",
            "Col_Value": "值",
            "Col_Unit": "单位",
            "Col_Count": "数量",
            "Col_Airway": "航线",
            "Col_PatrolCount": "巡逻数",
            "Col_AutoPatrol": "自巡逻",
            "Col_ConfigName": "配置名称",
            "Col_Default": "Def",
            "Col_OnlyFull": "Full",
            "Col_WeaponName": "武器名称",
            "Col_Tech": "科技名称",
            "Col_Set": "Set",
            "Col_Add": "Add",
            "Col_Property": "升级项",
            "Col_Radar": "雷达名称",
            "Col_ModifierName": "修改器名称",
            "Menu_File": "文件",
            "Menu_Language": "语言",
            "Menu_Help": "帮助",
            "MenuItem_Import": "导入配置",
            "MenuItem_Export": "导出配置",
            "MenuItem_Exit": "退出",
            "MenuItem_About": "关于",
            "Lang_Chinese": "中文",
            "Lang_English": "English",
            "About_Title": "关于 ICBM: Escalation 单位代码生成器",
            "About_Content": "这是一个用于生成ICBM: Escalation游戏单位代码的工具。\n\n功能特性：\n• 多语言支持（中文/英文）\n• 直观的标签页界面\n• 完整的单位属性配置\n• 武器配置管理\n• 自动代码生成\n\n版本：1.0\n开发时间：2025年",
            "Msg_ConfirmClear": "确定要清除所有数据吗？此操作不可撤销。",
            "Msg_ConfirmDefault": "确定要填充默认值吗？这将覆盖当前数据。",
            "Msg_RequiredFields": "请确保所有必填字段已填写！",
            "Msg_Success": "操作成功",
            "Msg_Error": "错误",
            "Msg_Warning": "警告",
            "Msg_SelectConfig": "请选择配置！",
            "Msg_SelectWeapon": "请选择武器！",
            "Msg_AssociationExists": "关联已存在：\n配置：{ConfigName}\n武器：{WeaponName}",
            "Msg_AssociationAdded": "关联已添加！",
            "Msg_ClearAllAssociations": "确定要清除所有关联吗？",
            "Msg_ConfigNameEmpty": "配置名称不能为空或为Default！",
            "Msg_ConfigNameExists": "配置名称已存在！",
            "Msg_CannotDeleteDefault": "不能删除Default配置！",
            "Msg_CannotModifyDefaultName": "不能修改Default配置的名称！",
            "Msg_SelectConfigFirst": "请先选择一个配置！",
            "Msg_WeaponNameCountRequired": "武器名称和数量不能为空！",
            "Msg_ConfigNameRequired": "配置名称不能为空！",
            "Msg_MissingFields": "以下必填项不能为空：\n{fields}",
            "Msg_UpgradeExists": "升级项已存在：\n科技：{Tech}\n升级项：{Property}",
            "Msg_CodeCopied": "代码已复制到剪贴板",
            "Msg_CodeSaved": "代码已保存到 {FilePath}",
            "Msg_LanguageChanged": "Language changed successfully! / 语言切换成功！"
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
            "Group_AllowedProduction": "Allowed Production",
            "Group_AllowedCarry": "Allowed Carry",
            "Group_UpgradeItems": "Upgrade Items (ImprovedBy)",
            "Group_StateSettings": "State Settings",
            "Group_AutoShift": "Auto Shift Settings",
            "Group_AirwayConfig": "Airway Configuration",
            "Group_SubUnitConfig": "SubUnit Configuration",
            "Label_GlobalName": "Global Name:",
            "Label_Tech": "Tech Reference:",
            "Label_Type": "Unit Type:",
            "Label_Class": "Unit Class:",
            "Label_Movie": "Topdown Path:",
            "Label_AbstractMovie": "Abstract Path:",
            "Label_Model": "3D Model Path:",
            "Label_Icon": "Icon Path:",
            "Label_RoundIcon": "Round Icon:",
            "Label_DrawSize": "Draw Size:",
            "Label_AbstractDrawSize": "Abstract Size:",
            "Label_ModelDrawSize": "Model Size:",
            "Label_Sound": "Sound Code:",
            "Label_SoundVolume": "Sound Volume:",
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
            "Label_Unit": "Unit",
            "Label_TechName": "Tech Name:",
            "Label_UpgradeProperty": "Upgrade Property:",
            "Label_Value": "Value:",
            "Label_SetValue": "Set (Modify Value)",
            "Label_AddValue": "Add (Increase Value)",
            "Label_UnitName": "Unit Name:",
            "Label_Count": "Count:",
            "Label_Airway": "Airway:",
            "Label_Patrol": "Patrol:",
            "Label_AutoPatrol": "Auto Patrol",
            "Label_ConfigName": "Config Name:",
            "Label_WeaponName": "Weapon Name:",
            "Label_LaunchCount": "Launch Count:",
            "Label_Interval": "Interval:",
            "Label_RadarName": "Radar Name:",
            "Label_Modifier": "Modifier:",
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
            "Btn_CopyCode": "Copy Code",
            "Btn_SaveToFile": "Save to File",
            "Btn_Close": "Close",
            "Col_Parameter": "Parameter",
            "Col_Value": "Value",
            "Col_Unit": "Unit",
            "Col_Count": "Count",
            "Col_Airway": "Airway",
            "Col_PatrolCount": "Patrol",
            "Col_AutoPatrol": "AutoPatrol",
            "Col_ConfigName": "Config Name",
            "Col_Default": "Def",
            "Col_OnlyFull": "Full",
            "Col_WeaponName": "Weapon Name",
            "Col_Tech": "Tech Name",
            "Col_Set": "Set",
            "Col_Add": "Add",
            "Col_Property": "Property",
            "Col_Radar": "Radar Name",
            "Col_ModifierName": "Modifier Name",
            "Menu_File": "File",
            "Menu_Language": "Language",
            "Menu_Help": "Help",
            "MenuItem_Import": "Import Configuration",
            "MenuItem_Export": "Export Configuration",
            "MenuItem_Exit": "Exit",
            "MenuItem_About": "About",
            "Lang_Chinese": "中文",
            "Lang_English": "English",
            "About_Title": "About ICBM: Escalation Unit Code Generator",
            "About_Content": "This is a tool for generating unit codes for the ICBM: Escalation game.\n\nFeatures:\n• Multi-language support (Chinese/English)\n• Intuitive tabbed interface\n• Complete unit property configuration\n• Weapon configuration management\n• Automatic code generation\n\nVersion: 1.0\nDevelopment: 2025",
            "Msg_ConfirmClear": "Are you sure you want to clear all data? This cannot be undone.",
            "Msg_ConfirmDefault": "Are you sure you want to fill default values? This will overwrite current data.",
            "Msg_RequiredFields": "Please ensure all required fields are filled!",
            "Msg_Success": "Success",
            "Msg_Error": "Error",
            "Msg_Warning": "Warning",
            "Msg_SelectConfig": "Please select a config!",
            "Msg_SelectWeapon": "Please select a weapon!",
            "Msg_AssociationExists": "Association already exists:\nConfig: {ConfigName}\nWeapon: {WeaponName}",
            "Msg_AssociationAdded": "Association added!",
            "Msg_ClearAllAssociations": "Are you sure you want to clear all associations?",
            "Msg_ConfigNameEmpty": "Config name cannot be empty or 'Default'!",
            "Msg_ConfigNameExists": "Config name already exists!",
            "Msg_CannotDeleteDefault": "Cannot delete Default config!",
            "Msg_CannotModifyDefaultName": "Cannot modify Default config name!",
            "Msg_SelectConfigFirst": "Please select a config first!",
            "Msg_WeaponNameCountRequired": "Weapon name and count cannot be empty!",
            "Msg_ConfigNameRequired": "Config name cannot be empty!",
            "Msg_MissingFields": "The following required fields cannot be empty:\n{fields}",
            "Msg_UpgradeExists": "Upgrade already exists:\nTech: {Tech}\nProperty: {Property}",
            "Msg_CodeCopied": "Code copied to clipboard",
            "Msg_CodeSaved": "Code saved to {FilePath}",
            "Msg_LanguageChanged": "Language changed successfully! / 语言切换成功！"
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
        self.Root.resizable(True, True)  # 允许窗口调整大小
        self.Root.minsize(1024, 768)  # 设置最小尺寸
    
    def CreateWidgets(self):
        """创建所有控件"""
        # 创建菜单栏
        self.CreateMenuBar()
        
        # 按钮区域框架 - 固定在底部
        self.ButtonFrame = ttk.Frame(self.Root)
        self.ButtonFrame.pack(side="bottom", fill="x", padx=5, pady=5)
        
        # 主内容框架 - 填充剩余空间
        self.ContentFrame = ttk.Frame(self.Root)
        self.ContentFrame.pack(side="top", fill="both", expand=True)
        
        # 标签页
        self.Notebook = ttk.Notebook(self.ContentFrame)
        self.Notebook.pack(fill="both", expand=True, padx=5, pady=5)
        
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
    
    def CreateMenuBar(self):
        """创建菜单栏"""
        MenuBar = tk.Menu(self.Root)
        self.Root.config(menu=MenuBar)
        
        # 文件菜单
        FileMenu = tk.Menu(MenuBar, tearoff=0)
        MenuBar.add_cascade(label=self.Lang.Get("Menu_File"), menu=FileMenu)
        FileMenu.add_command(label=self.Lang.Get("MenuItem_Import"), command=self.ImportConfig)
        FileMenu.add_command(label=self.Lang.Get("MenuItem_Export"), command=self.ExportConfig)
        FileMenu.add_separator()
        FileMenu.add_command(label=self.Lang.Get("MenuItem_Exit"), command=self.Root.quit)
        
        # 语言菜单
        LanguageMenu = tk.Menu(MenuBar, tearoff=0)
        MenuBar.add_cascade(label=self.Lang.Get("Menu_Language"), menu=LanguageMenu)
        
        # 创建语言选项的变量
        self.LanguageVar = tk.StringVar(value=self.Lang.CurrentLanguage)
        
        # 添加语言选项
        for LangCode in self.Lang.GetAvailableLanguages():
            LangName = self.Lang.Get("Lang_Chinese") if LangCode == "zh_CN" else self.Lang.Get("Lang_English")
            LanguageMenu.add_radiobutton(
                label=LangName,
                variable=self.LanguageVar,
                value=LangCode,
                command=lambda code=LangCode: self.ChangeLanguage(code)
            )
        
        # 帮助菜单
        HelpMenu = tk.Menu(MenuBar, tearoff=0)
        MenuBar.add_cascade(label=self.Lang.Get("Menu_Help"), menu=HelpMenu)
        HelpMenu.add_command(label=self.Lang.Get("MenuItem_About"), command=self.ShowAbout)
    
    def ChangeLanguage(self, LangCode):
        """切换语言"""
        self.Lang.SetLanguage(LangCode)
        self.SaveLanguageSettings()
        self.UpdateUI()
        messagebox.showinfo(
            self.Lang.Get("Msg_Success"),
            "Language changed successfully! / 语言切换成功！"
        )
    
    def ShowAbout(self):
        """显示关于对话框"""
        messagebox.showinfo(self.Lang.Get("About_Title"), self.Lang.Get("About_Content"))
    
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
            # 获取所有标签页的ID和索引
            for i in range(self.Notebook.index("end")):
                # 根据索引设置新的标题
                if i == 0:
                    self.Notebook.tab(i, text=self.Lang.Get("Tab_BasicInfo"))
                elif i == 1:
                    self.Notebook.tab(i, text=self.Lang.Get("Tab_Behavior"))
                elif i == 2:
                    self.Notebook.tab(i, text=self.Lang.Get("Tab_SubUnit"))
                elif i == 3:
                    self.Notebook.tab(i, text=self.Lang.Get("Tab_Weapon"))
                elif i == 4:
                    self.Notebook.tab(i, text=self.Lang.Get("Tab_RadarModifier"))
                elif i == 5:
                    self.Notebook.tab(i, text=self.Lang.Get("Tab_StateSwitch"))
                elif i == 6:
                    self.Notebook.tab(i, text=self.Lang.Get("Tab_Upgrade"))
        
        # 更新工具栏按钮文本
        if hasattr(self, 'LanguageCombo'):
            self.LanguageCombo.set(self.Lang.CurrentLanguage)
        
        # 重新创建基本标签页以更新文本
        self.RecreateBasicInfoTab()
        
        # 更新底部按钮文本
        self.UpdateBottomButtons()
        
        # 更新自定义参数表格标题
        if hasattr(self, 'CustomParamsTable'):
            self.CustomParamsTable.heading("Parameter", text=self.Lang.Get("Col_Parameter"))
            self.CustomParamsTable.heading("Value", text=self.Lang.Get("Col_Value"))
    
    def RecreateBasicInfoTab(self):
        """重新创建基本信息标签页以更新文本"""
        # 保存当前标签页选择
        current_tab = self.Notebook.index("current")
        
        # 移除旧的标签页
        for tab_id in self.Notebook.tabs():
            self.Notebook.forget(tab_id)
        
        # 重新创建所有标签页
        self.CreateBasicInfoTab()
        self.CreateBehaviorTab()
        self.CreateSubUnitTab()
        self.CreateWeaponTab()
        self.CreateRadarModifierTab()
        self.CreateStateSwitchTab()
        self.CreateUpgradeTab()
        
        # 恢复标签页选择
        self.Notebook.select(current_tab)
    
    def UpdateBottomButtons(self):
        """更新底部按钮文本"""
        if hasattr(self, 'BottomButtons'):
            for button, text_key in self.BottomButtons:
                button.config(text=self.Lang.Get(text_key))
    
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
            ("SoundVolume", "Label_SoundVolume", "entry", None),
            ("LaunchMeSound", "Label_LaunchMeSound", "entry", None)
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
            height=9
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
        GroupFrame = ttk.LabelFrame(Frame, text=self.Lang.Get("Group_BehaviorConfig"))
        GroupFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # 行为选项定义：(变量名, 翻译键, 代码键名, 类型, 隐藏规则)
        # 类型: Boolean=输出Yes/No, Existed=勾选时只输出键名
        # 隐藏规则: Normal=总是输出, HideWhenFalse=False时不输出
        self.BehaviorOptions = [
            ("AlwaysVisibleOnEnemyTerritory", "Behavior_AlwaysVisibleOnEnemyTerritory", "AlwaysVisibleOnEnemyTerritory", "Boolean", "Normal"),
            ("DoesNotTriggerWarWhenAttacked", "Behavior_DoesNotTriggerWarWhenAttacked", "DoesNotTriggerWarWhenAttacked", "Boolean", "HideWhenFalse"),
            ("CanCrossBorderDuringPeaceTime", "Behavior_CanCrossBorderDuringPeaceTime", "CanCrossBorderDuringPeaceTime", "Boolean", "Normal"),
            ("CanCrossBorder", "Behavior_CanCrossBorder", "CanCrossBorder", "Boolean", "Normal"),
            ("DoesNotTriggerWarOnAttack", "Behavior_DoesNotTriggerWarOnAttack", "DoesNotTriggerWarOnAttack", "Boolean", "HideWhenFalse"),
            ("ReportAsHosted", "Behavior_ReportAsHosted", "ReportAsHosted", "Boolean", "HideWhenFalse"),
            ("TargetInPlanner", "Behavior_TargetInPlanner", "TargetInPlanner", "Boolean", "HideWhenFalse"),
            ("AttackerInPlanner", "Behavior_AttackerInPlanner", "AttackerInPlanner", "Existed", "HideWhenFalse"),
            ("CanAccessGlobalStorage", "Behavior_CanAccessGlobalStorage", "CanAccessGlobalStorage", "Boolean", "HideWhenFalse"),
            ("CanAccessWeaponStockpile", "Behavior_CanAccessWeaponStockpile", "CanAccessWeaponStockpile", "Boolean", "HideWhenFalse"),
            ("CanAccessUnitStockpile", "Behavior_CanAccessUnitStockpile", "CanAccessUnitStockpile", "Boolean", "HideWhenFalse"),
            ("CanHangInTheAir", "Behavior_CanHangInTheAir", "CanHangInTheAir", "Boolean", "HideWhenFalse"),
            ("HideOwnership", "Behavior_HideOwnership", "HideOwnership", "Boolean", "HideWhenFalse"),
            ("CanPatrolPoint", "Behavior_CanPatrolPoint", "CanPatrolPoint", "Boolean", "HideWhenFalse"),
            ("AutoReturn", "Behavior_AutoReturn", "AutoReturn", "Boolean", "HideWhenFalse"),
            ("ProducedByAnotherUnit", "Behavior_ProducedByAnotherUnit", "ProducedByAnotherUnit", "Boolean", "HideWhenFalse"),
            ("FixedRotationAngle", "Behavior_FixedRotationAngle", "FixedRotationAngle", "Boolean", "HideWhenFalse"),
            ("AttackOnMove", "Behavior_AttackOnMove", "AttackOnMove", "Boolean", "HideWhenFalse"),
            ("ShowDisabledOnDeploymentMarker", "Behavior_ShowDisabledOnDeploymentMarker", "ShowDisabledOnDeploymentMarker", "Boolean", "HideWhenFalse"),
            ("DestroyOnFactionSurrender", "Behavior_DestroyOnFactionSurrender", "DestroyOnFactionSurrender", "Boolean", "HideWhenFalse"),
            ("HiddenFromAllies", "Behavior_HiddenFromAllies", "HiddenFromAllies", "Existed", "HideWhenFalse"),
            ("AttackIfDestroyed", "Behavior_AttackIfDestroyed", "AttackIfDestroyed", "Existed", "HideWhenFalse"),
            ("NoAutoAttack", "Behavior_NoAutoAttack", "NoAutoAttack", "Existed", "HideWhenFalse"),
            ("NoAutoAttackSub", "Behavior_NoAutoAttackSub", "NoAutoAttackSub", "Existed", "HideWhenFalse"),
            ("Slave", "Behavior_Slave", "Slave", "Boolean", "HideWhenFalse"),
            ("NoAutoDeploy", "Behavior_NoAutoDeploy", "NoAutoDeploy", "Boolean", "HideWhenFalse"),
            ("ExecuteOrdersWhenBesieged", "Behavior_ExecuteOrdersWhenBesieged", "ExecuteOrdersWhenBesieged", "Boolean", "HideWhenFalse"),
            ("HideAbstract", "Behavior_HideAbstract", "HideAbstract", "Boolean", "HideWhenFalse")
        ]
        
        # 创建复选框
        self.BehaviorVars = {}
        ColCount = 3  # 每行显示3个
        for i, (VarName, LangKey, CodeKey, BType, HideRule) in enumerate(self.BehaviorOptions):
            Row = i // ColCount
            Col = i % ColCount
            
            Var = tk.BooleanVar()
            self.BehaviorVars[VarName] = {
                "Var": Var,
                "CodeKey": CodeKey,
                "Type": BType,
                "HideRule": HideRule
            }
            
            Checkbox = ttk.Checkbutton(GroupFrame, text=self.Lang.Get(LangKey), variable=Var)
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
        GroupFrame = ttk.LabelFrame(ParentFrame, text=self.Lang.Get("Group_AllowedProduction"))
        GroupFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(GroupFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(InputFrame, text=self.Lang.Get("Label_Unit")).pack(side="left", padx=2)
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
        self.ProducesTable.heading("Unit", text=self.Lang.Get("Label_Unit").rstrip(":"))
        self.ProducesTable.column("Unit", width=200)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.ProducesTable.yview)
        self.ProducesTable.configure(yscrollcommand=Scrollbar.set)
        self.ProducesTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        # 按钮
        BtnFrame = ttk.Frame(GroupFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadProduces).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveProduces).pack(side="left", padx=2)
    
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
        GroupFrame = ttk.LabelFrame(ParentFrame, text=self.Lang.Get("Group_AllowedCarry"))
        GroupFrame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(GroupFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(InputFrame, text=self.Lang.Get("Label_Unit")).pack(side="left", padx=2)
        self.CanCarryEntry = ttk.Combobox(InputFrame, values=self.DB.Get("Units"), width=22)
        self.CanCarryEntry.pack(side="left", padx=2)
        ttk.Button(InputFrame, text="+", width=3, command=self.AddCanCarry).pack(side="left", padx=2)
        ttk.Button(InputFrame, text="-", width=3, command=self.DeleteCanCarry).pack(side="left", padx=2)
        
        # 表格
        TableFrame = ttk.Frame(GroupFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.CanCarryTable = ttk.Treeview(TableFrame, columns=("Unit",), show="headings", height=8)
        self.CanCarryTable.heading("Unit", text=self.Lang.Get("Label_Unit").rstrip(":"))
        self.CanCarryTable.column("Unit", width=200)
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.CanCarryTable.yview)
        self.CanCarryTable.configure(yscrollcommand=Scrollbar.set)
        self.CanCarryTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        BtnFrame = ttk.Frame(GroupFrame)
        BtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadCanCarry).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveCanCarry).pack(side="left", padx=2)
    
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
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadAirway).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveAirway).pack(side="left", padx=2)
    
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
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadHostAircraft).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveHostAircraft).pack(side="left", padx=2)
    
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
        Frame.columnconfigure(1, weight=2)
        Frame.rowconfigure(0, weight=1)
        
        # 初始化数据结构
        # ConfigData: {配置名称: {"Default": bool, "OnlyFull": bool, "Weapons": []}}
        self.ConfigData = {
            "Default": {"Default": False, "OnlyFull": False, "Weapons": []}
        }
        self.CurrentSelectedConfig = "Default"
        
        # 左侧：配置列表
        self.CreateConfigPanel(Frame)
        
        # 右侧：武器列表
        self.CreateWeaponPanel(Frame)
    
    def CreateConfigPanel(self, ParentFrame):
        """创建配置面板（左侧）"""
        ConfigFrame = ttk.LabelFrame(ParentFrame, text="武器配置 (Config)")
        ConfigFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(ConfigFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(InputFrame, text="配置名称:").grid(row=0, column=0, padx=2, sticky="w")
        self.ConfigNameEntry = ttk.Entry(InputFrame, width=20)
        self.ConfigNameEntry.grid(row=0, column=1, padx=2)
        
        # 复选框
        CheckFrame = ttk.Frame(InputFrame)
        CheckFrame.grid(row=1, column=0, columnspan=2, pady=5)
        
        self.ConfigDefaultVar = tk.BooleanVar()
        self.ConfigOnlyFullVar = tk.BooleanVar()
        
        ttk.Checkbutton(CheckFrame, text="Default", variable=self.ConfigDefaultVar).pack(side="left", padx=5)
        ttk.Checkbutton(CheckFrame, text="OnlyFull", variable=self.ConfigOnlyFullVar).pack(side="left", padx=5)
        
        # 按钮
        BtnFrame = ttk.Frame(InputFrame)
        BtnFrame.grid(row=0, column=2, rowspan=2, padx=5)
        ttk.Button(BtnFrame, text="+", width=3, command=self.AddConfig).pack(pady=2)
        ttk.Button(BtnFrame, text="-", width=3, command=self.DeleteConfig).pack(pady=2)
        
        # 配置表格
        TableFrame = ttk.Frame(ConfigFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        
        Columns = ("Name", "Default", "OnlyFull")
        self.ConfigTable = ttk.Treeview(TableFrame, columns=Columns, show="headings", height=23)
        self.ConfigTable.heading("Name", text="配置名称")
        self.ConfigTable.heading("Default", text="Def")
        self.ConfigTable.heading("OnlyFull", text="Full")
        self.ConfigTable.column("Name", width=200)
        self.ConfigTable.column("Default", width=50)
        self.ConfigTable.column("OnlyFull", width=50)
        
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.ConfigTable.yview)
        self.ConfigTable.configure(yscrollcommand=Scrollbar.set)
        self.ConfigTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        # 插入默认配置
        self.ConfigTable.insert("", 0, values=("Default", ""))
        
        # 绑定选择事件
        self.ConfigTable.bind("<<TreeviewSelect>>", self.OnConfigSelect)
        
        # 操作按钮
        OpFrame = ttk.Frame(ConfigFrame)
        OpFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_MoveUp"), width=3, command=self.MoveConfigUp).pack(side="left", padx=2)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_MoveDown"), width=3, command=self.MoveConfigDown).pack(side="left", padx=2)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadConfig).pack(side="left", padx=2)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveConfig).pack(side="left", padx=2)
    
    def CreateWeaponPanel(self, ParentFrame):
        """创建武器面板（右侧）"""
        WeaponFrame = ttk.LabelFrame(ParentFrame, text="武器列表 (Weapon)")
        WeaponFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(WeaponFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(InputFrame, text="武器名称:").grid(row=0, column=0, padx=2, sticky="w")
        self.WeaponNameEntry = ttk.Combobox(InputFrame, values=self.DB.Get("Weapons"), width=18)
        self.WeaponNameEntry.grid(row=0, column=1, padx=2)
        
        ttk.Label(InputFrame, text="数量:").grid(row=0, column=2, padx=2)
        self.WeaponCountEntry = ttk.Entry(InputFrame, width=8)
        self.WeaponCountEntry.grid(row=0, column=3, padx=2)
        
        ttk.Label(InputFrame, text="Launch:").grid(row=1, column=0, padx=2, sticky="w")
        self.WeaponLaunchEntry = ttk.Entry(InputFrame, width=8)
        self.WeaponLaunchEntry.grid(row=1, column=1, padx=2)
        
        ttk.Label(InputFrame, text="Time:").grid(row=1, column=2, padx=2)
        self.WeaponTimeEntry = ttk.Entry(InputFrame, width=8)
        self.WeaponTimeEntry.grid(row=1, column=3, padx=2)
        
        # 复选框
        CheckFrame = ttk.Frame(InputFrame)
        CheckFrame.grid(row=2, column=0, columnspan=4, pady=5)
        
        self.WeaponAutoEngageVar = tk.BooleanVar()
        self.WeaponPrincipalVar = tk.BooleanVar()
        self.WeaponDefaultOffVar = tk.BooleanVar()
        
        ttk.Checkbutton(CheckFrame, text="AutoEngage", variable=self.WeaponAutoEngageVar).pack(side="left", padx=5)
        ttk.Checkbutton(CheckFrame, text="Principal", variable=self.WeaponPrincipalVar).pack(side="left", padx=5)
        ttk.Checkbutton(CheckFrame, text="DefaultOff", variable=self.WeaponDefaultOffVar).pack(side="left", padx=5)
        
        # 按钮
        BtnFrame = ttk.Frame(InputFrame)
        BtnFrame.grid(row=0, column=4, rowspan=3, padx=5)
        ttk.Button(BtnFrame, text="+", width=3, command=self.AddWeapon).pack(pady=2)
        ttk.Button(BtnFrame, text="-", width=3, command=self.DeleteWeapon).pack(pady=2)
        
        # 武器表格
        TableFrame = ttk.Frame(WeaponFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        
        Columns = ("Name", "Count", "Launch", "Time", "Auto", "Prin", "Off")
        self.WeaponTable = ttk.Treeview(TableFrame, columns=Columns, show="headings", height=20)
        self.WeaponTable.heading("Name", text="武器名称")
        self.WeaponTable.heading("Count", text="数量")
        self.WeaponTable.heading("Launch", text="Launch")
        self.WeaponTable.heading("Time", text="Time")
        self.WeaponTable.heading("Auto", text="Auto")
        self.WeaponTable.heading("Prin", text="Prin")
        self.WeaponTable.heading("Off", text="Off")
        self.WeaponTable.column("Name", width=150)
        self.WeaponTable.column("Count", width=60)
        self.WeaponTable.column("Launch", width=50)
        self.WeaponTable.column("Time", width=50)
        self.WeaponTable.column("Auto", width=40)
        self.WeaponTable.column("Prin", width=40)
        self.WeaponTable.column("Off", width=40)
        
        Scrollbar = ttk.Scrollbar(TableFrame, orient="vertical", command=self.WeaponTable.yview)
        self.WeaponTable.configure(yscrollcommand=Scrollbar.set)
        self.WeaponTable.pack(side="left", fill="both", expand=True)
        Scrollbar.pack(side="right", fill="y")
        
        # 操作按钮
        OpFrame = ttk.Frame(WeaponFrame)
        OpFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_MoveUp"), width=3, command=self.MoveWeaponUp).pack(side="left", padx=2)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_MoveDown"), width=3, command=self.MoveWeaponDown).pack(side="left", padx=2)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadWeapon).pack(side="left", padx=2)
        ttk.Button(OpFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveWeapon).pack(side="left", padx=2)
    
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
        if not Name or Name == "Default":
            messagebox.showwarning("警告", "配置名称不能为空或为Default！")
            return
        
        # 检查是否已存在
        for Item in self.ConfigTable.get_children():
            if self.ConfigTable.item(Item, "values")[0] == Name:
                messagebox.showwarning("警告", "配置名称已存在！")
                return
        
        DefaultStr = "√" if self.ConfigDefaultVar.get() else ""
        OnlyFullStr = "√" if self.ConfigOnlyFullVar.get() else ""
        
        self.ConfigTable.insert("", tk.END, values=(Name, DefaultStr, OnlyFullStr))
        self.ConfigData[Name] = {
            "Default": self.ConfigDefaultVar.get(),
            "OnlyFull": self.ConfigOnlyFullVar.get(),
            "Weapons": []
        }
        self.ConfigNameEntry.delete(0, tk.END)
        self.ConfigDefaultVar.set(False)
        self.ConfigOnlyFullVar.set(False)
    
    def DeleteConfig(self):
        """删除武器配置"""
        Selected = self.ConfigTable.selection()
        if not Selected:
            return
        
        Values = self.ConfigTable.item(Selected[0], "values")
        if not Values or Values[0] == "Default":
            messagebox.showwarning("警告", "不能删除Default配置！")
            return
        
        ConfigName = Values[0]
        if ConfigName in self.ConfigData:
            del self.ConfigData[ConfigName]
        self.ConfigTable.delete(Selected[0])
        
        # 清空武器表格
        for Item in self.WeaponTable.get_children():
            self.WeaponTable.delete(Item)
    
    def OnConfigSelect(self, Event=None):
        """配置选择事件"""
        Selected = self.ConfigTable.selection()
        if not Selected:
            return
        
        Values = self.ConfigTable.item(Selected[0], "values")
        if not Values:
            return
        
        ConfigName = Values[0]
        self.CurrentSelectedConfig = ConfigName
        
        # 更新武器表格
        for Item in self.WeaponTable.get_children():
            self.WeaponTable.delete(Item)
        
        if ConfigName in self.ConfigData:
            for WeaponData in self.ConfigData[ConfigName]["Weapons"]:
                self.WeaponTable.insert("", tk.END, values=(
                    WeaponData["Name"],
                    WeaponData["Count"],
                    WeaponData["Launch"],
                    WeaponData["Time"],
                    "√" if WeaponData["AutoEngage"] else "",
                    "√" if WeaponData["Principal"] else "",
                    "√" if WeaponData["DefaultOff"] else ""
                ))
    
    def LoadConfig(self):
        """读取选中的配置"""
        Selected = self.ConfigTable.selection()
        if not Selected:
            return
        
        Values = self.ConfigTable.item(Selected[0], "values")
        if not Values:
            return
        
        ConfigName = Values[0]
        self.ConfigNameEntry.delete(0, tk.END)
        self.ConfigNameEntry.insert(0, ConfigName)
        
        self.ConfigDefaultVar.set(Values[1] == "√")
        self.ConfigOnlyFullVar.set(Values[2] == "√")
    
    def SaveConfig(self):
        """保存到选中的配置"""
        Selected = self.ConfigTable.selection()
        if not Selected:
            self.AddConfig()
            return
        
        Name = self.ConfigNameEntry.get().strip()
        if not Name:
            messagebox.showwarning("警告", "配置名称不能为空！")
            return
        
        OldValues = self.ConfigTable.item(Selected[0], "values")
        OldName = OldValues[0]
        
        if OldName == "Default" and Name != "Default":
            messagebox.showwarning("警告", "不能修改Default配置的名称！")
            return
        
        DefaultStr = "√" if self.ConfigDefaultVar.get() else ""
        OnlyFullStr = "√" if self.ConfigOnlyFullVar.get() else ""
        
        self.ConfigTable.item(Selected[0], values=(Name, DefaultStr, OnlyFullStr))
        
        if OldName != Name and OldName in self.ConfigData:
            self.ConfigData[Name] = self.ConfigData.pop(OldName)
        
        if Name in self.ConfigData:
            self.ConfigData[Name]["Default"] = self.ConfigDefaultVar.get()
            self.ConfigData[Name]["OnlyFull"] = self.ConfigOnlyFullVar.get()
    
    def AddWeapon(self):
        """添加武器到当前配置"""
        if not self.CurrentSelectedConfig:
            messagebox.showwarning("警告", "请先选择一个配置！")
            return
        
        Name = self.WeaponNameEntry.get().strip()
        Count = self.WeaponCountEntry.get().strip()
        
        if not Name or not Count:
            messagebox.showwarning("警告", "武器名称和数量不能为空！")
            return
        
        Launch = self.WeaponLaunchEntry.get().strip()
        Time = self.WeaponTimeEntry.get().strip()
        
        WeaponData = {
            "Name": Name,
            "Count": Count,
            "Launch": Launch,
            "Time": Time,
            "AutoEngage": self.WeaponAutoEngageVar.get(),
            "Principal": self.WeaponPrincipalVar.get(),
            "DefaultOff": self.WeaponDefaultOffVar.get()
        }
        
        self.ConfigData[self.CurrentSelectedConfig]["Weapons"].append(WeaponData)
        
        self.WeaponTable.insert("", tk.END, values=(
            Name, Count, Launch, Time,
            "√" if WeaponData["AutoEngage"] else "",
            "√" if WeaponData["Principal"] else "",
            "√" if WeaponData["DefaultOff"] else ""
        ))
        
        self.ClearWeaponInputs()
    
    def DeleteWeapon(self):
        """删除武器"""
        if not self.CurrentSelectedConfig:
            return
        
        Selected = self.WeaponTable.selection()
        if not Selected:
            return
        
        Index = self.WeaponTable.index(Selected[0])
        if Index < len(self.ConfigData[self.CurrentSelectedConfig]["Weapons"]):
            del self.ConfigData[self.CurrentSelectedConfig]["Weapons"][Index]
        
        self.WeaponTable.delete(Selected[0])
    
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
        if not self.CurrentSelectedConfig:
            return
        
        Selected = self.WeaponTable.selection()
        if not Selected:
            self.AddWeapon()
            return
        
        Name = self.WeaponNameEntry.get().strip()
        Count = self.WeaponCountEntry.get().strip()
        
        if not Name or not Count:
            messagebox.showwarning("警告", "武器名称和数量不能为空！")
            return
        
        Index = self.WeaponTable.index(Selected[0])
        
        WeaponData = {
            "Name": Name,
            "Count": Count,
            "Launch": self.WeaponLaunchEntry.get().strip(),
            "Time": self.WeaponTimeEntry.get().strip(),
            "AutoEngage": self.WeaponAutoEngageVar.get(),
            "Principal": self.WeaponPrincipalVar.get(),
            "DefaultOff": self.WeaponDefaultOffVar.get()
        }
        
        self.ConfigData[self.CurrentSelectedConfig]["Weapons"][Index] = WeaponData
        
        self.WeaponTable.item(Selected[0], values=(
            Name, Count, WeaponData["Launch"], WeaponData["Time"],
            "√" if WeaponData["AutoEngage"] else "",
            "√" if WeaponData["Principal"] else "",
            "√" if WeaponData["DefaultOff"] else ""
        ))
        
        self.ClearWeaponInputs()
    
    def MoveConfigUp(self):
        """向上移动配置"""
        Selected = self.ConfigTable.selection()
        if not Selected:
            return
        
        Values = self.ConfigTable.item(Selected[0], "values")
        if Values[0] == "Default":
            messagebox.showwarning("警告", "Default配置必须保持在第一位！")
            return
        
        Index = self.ConfigTable.index(Selected[0])
        if Index > 1:  # 不能移动到Default之前
            self.ConfigTable.move(Selected[0], "", Index - 1)
    
    def MoveConfigDown(self):
        """向下移动配置"""
        Selected = self.ConfigTable.selection()
        if not Selected:
            return
        
        Values = self.ConfigTable.item(Selected[0], "values")
        if Values[0] == "Default":
            messagebox.showwarning("警告", "Default配置必须保持在第一位！")
            return
        
        Index = self.ConfigTable.index(Selected[0])
        if Index < len(self.ConfigTable.get_children()) - 1:
            self.ConfigTable.move(Selected[0], "", Index + 1)
    
    def MoveWeaponUp(self):
        """向上移动武器"""
        if not self.CurrentSelectedConfig:
            return
        
        Selected = self.WeaponTable.selection()
        if not Selected:
            return
        
        Index = self.WeaponTable.index(Selected[0])
        if Index > 0:
            # 交换数据
            Weapons = self.ConfigData[self.CurrentSelectedConfig]["Weapons"]
            Weapons[Index], Weapons[Index-1] = Weapons[Index-1], Weapons[Index]
            # 移动表格项
            self.WeaponTable.move(Selected[0], "", Index - 1)
    
    def MoveWeaponDown(self):
        """向下移动武器"""
        if not self.CurrentSelectedConfig:
            return
        
        Selected = self.WeaponTable.selection()
        if not Selected:
            return
        
        Index = self.WeaponTable.index(Selected[0])
        Weapons = self.ConfigData[self.CurrentSelectedConfig]["Weapons"]
        if Index < len(Weapons) - 1:
            # 交换数据
            Weapons[Index], Weapons[Index+1] = Weapons[Index+1], Weapons[Index]
            # 移动表格项
            self.WeaponTable.move(Selected[0], "", Index + 1)
    
    def AddWeaponConfigAssociation(self):
        """添加武器配置关联"""
        ConfigName = self.AssocConfigCombo.get()
        WeaponName = self.AssocWeaponCombo.get()
        
        # 验证必填项
        if not ConfigName:
            messagebox.showwarning(self.Lang.Get("Msg_Warning"), "请选择配置！")
            return
        if not WeaponName:
            messagebox.showwarning(self.Lang.Get("Msg_Warning"), "请选择武器！")
            return
            
        # 检查是否已存在
        for Item in self.WeaponConfigTable.get_children():
            Values = self.WeaponConfigTable.item(Item, "values")
            if Values and Values[0] == ConfigName and Values[1] == WeaponName:
                messagebox.showwarning(self.Lang.Get("Msg_Warning"), 
                    f"关联已存在：\n配置：{ConfigName}\n武器：{WeaponName}")
                return
        
        self.WeaponConfigTable.insert("", tk.END, values=(ConfigName, WeaponName))
        self.WeaponConfigAssociations.append((ConfigName, WeaponName))
        
        # 清空选择
        self.AssocConfigCombo.set("")
        self.AssocWeaponCombo.set("")
        
        messagebox.showinfo(self.Lang.Get("Msg_Success"), "关联已添加！")
    
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
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadRadar).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveRadar).pack(side="left", padx=2)
        
        # 修改器配置
        ModifierFrame = ttk.LabelFrame(Frame, text="修改器配置")
        ModifierFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        ModInputFrame = ttk.Frame(ModifierFrame)
        ModInputFrame.pack(fill="x", padx=5, pady=5)
        ttk.Label(ModInputFrame, text="修改器:").pack(side="left", padx=2)
        self.ModifierNameEntry = ttk.Combobox(ModInputFrame, values=self.DB.Get("Modifiers"), width=25)
        self.ModifierNameEntry.pack(side="left", padx=2)
        ttk.Button(ModInputFrame, text="+", width=3, command=self.AddModifier).pack(side="left", padx=2)
        ttk.Button(ModInputFrame, text="-", width=3, command=self.DeleteModifier).pack(side="left", padx=2)
        
        ModTableFrame = ttk.Frame(ModifierFrame)
        ModTableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.ModifierTable = ttk.Treeview(ModTableFrame, columns=("Name",), show="headings", height=18)
        self.ModifierTable.heading("Name", text="修改器名称")
        self.ModifierTable.column("Name", width=360)
        ModScrollbar = ttk.Scrollbar(ModTableFrame, orient="vertical", command=self.ModifierTable.yview)
        self.ModifierTable.configure(yscrollcommand=ModScrollbar.set)
        self.ModifierTable.pack(side="left", fill="both", expand=True)
        ModScrollbar.pack(side="right", fill="y")
        
        ModBtnFrame = ttk.Frame(ModifierFrame)
        ModBtnFrame.pack(fill="x", padx=5, pady=5)
        ttk.Button(ModBtnFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadModifier).pack(side="left", padx=2)
        ttk.Button(ModBtnFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveModifier).pack(side="left", padx=2)
    
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
            self.ModifierTable.insert("", tk.END, values=(Name,))
            self.ModifierNameEntry.delete(0, tk.END)
    
    def DeleteModifier(self):
        Selected = self.ModifierTable.selection()
        if Selected:
            self.ModifierTable.delete(Selected[0])
    
    def LoadModifier(self):
        Selected = self.ModifierTable.selection()
        if Selected:
            Values = self.ModifierTable.item(Selected[0], "values")
            self.ModifierNameEntry.delete(0, tk.END)
            if Values:
                self.ModifierNameEntry.insert(0, Values[0])
    
    def SaveModifier(self):
        Selected = self.ModifierTable.selection()
        Name = self.ModifierNameEntry.get().strip()
        if not Selected:
            self.AddModifier()
        elif Name:
            self.ModifierTable.item(Selected[0], values=(Name,))
            self.ModifierNameEntry.delete(0, tk.END)
    
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
        
        # 状态名称
        StateFields = [
            ("HighState", "高状态名称:", 0),
            ("LowState", "低状态名称:", 1),
            ("TimeToHighState", "切换高状态时间:", 2),
            ("TimeToLowState", "切换低状态时间:", 3),
            ("HighStateStringIDX", "高状态字符串索引:", 4),
            ("LowStateStringIDX", "低状态字符串索引:", 5),
            ("StateStringIDX", "当前状态字符串索引:", 6),
            ("StateIcon", "状态图标路径:", 7),
            ("ToHighStateIcon", "切换高状态图标:", 8),
            ("ToLowStateIcon", "切换低状态图标:", 9),
            ("ToHighStateProcessingStringIDX", "高状态处理字符串:", 10),
            ("ToLowStateProcessingStringIDX", "低状态处理字符串:", 11),
            ("AutoOnRestDelay", "切换高状态延迟:", 12)
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
        UpgradeFrame = ttk.LabelFrame(Frame, text=self.Lang.Get("Group_UpgradeItems"))
        UpgradeFrame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # 输入区
        InputFrame = ttk.Frame(UpgradeFrame)
        InputFrame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(InputFrame, text=self.Lang.Get("Label_TechName")).grid(row=0, column=0, padx=2, sticky="w")
        self.UpgradeTechEntry = ttk.Combobox(InputFrame, values=self.DB.Get("Techs"), width=25)
        self.UpgradeTechEntry.grid(row=0, column=1, padx=2)
        
        # Set/Add复选框
        OptionsFrame = ttk.Frame(InputFrame)
        OptionsFrame.grid(row=0, column=2, padx=10)
        self.UpgradeSetVar = tk.BooleanVar()
        self.UpgradeAddVar = tk.BooleanVar()
        ttk.Checkbutton(OptionsFrame, text=self.Lang.Get("Label_SetValue"), variable=self.UpgradeSetVar).pack(anchor="w", pady=1)
        ttk.Checkbutton(OptionsFrame, text=self.Lang.Get("Label_AddValue"), variable=self.UpgradeAddVar).pack(anchor="w", pady=1)
        
        ttk.Label(InputFrame, text=self.Lang.Get("Label_UpgradeProperty")).grid(row=1, column=0, padx=2, sticky="w")
        self.UpgradePropertyEntry = ttk.Entry(InputFrame, width=25)
        self.UpgradePropertyEntry.grid(row=1, column=1, padx=2)
        
        ttk.Label(InputFrame, text=self.Lang.Get("Label_Value")).grid(row=1, column=2, padx=2, sticky="w")
        self.UpgradeValueEntry = ttk.Entry(InputFrame, width=15)
        self.UpgradeValueEntry.grid(row=1, column=3, padx=2)
        
        BtnInputFrame = ttk.Frame(InputFrame)
        BtnInputFrame.grid(row=0, column=4, rowspan=2, padx=5)
        ttk.Button(BtnInputFrame, text=self.Lang.Get("Btn_Add"), width=3, command=self.AddUpgrade).pack(pady=2)
        ttk.Button(BtnInputFrame, text=self.Lang.Get("Btn_Delete"), width=3, command=self.DeleteUpgrade).pack(pady=2)
        
        # 升级项表格
        TableFrame = ttk.Frame(UpgradeFrame)
        TableFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.UpgradeTable = ttk.Treeview(
            TableFrame, 
            columns=("Tech", "Set", "Add", "Property", "Value"), 
            show="headings", 
            height=20
        )
        self.UpgradeTable.heading("Tech", text=self.Lang.Get("Col_Tech"))
        self.UpgradeTable.heading("Set", text=self.Lang.Get("Col_Set"))
        self.UpgradeTable.heading("Add", text=self.Lang.Get("Col_Add"))
        self.UpgradeTable.heading("Property", text=self.Lang.Get("Col_Property"))
        self.UpgradeTable.heading("Value", text=self.Lang.Get("Label_Value").rstrip(":"))
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
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_MoveUp"), width=3, command=self.MoveUpgradeUp).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_MoveDown"), width=3, command=self.MoveUpgradeDown).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Load"), width=8, command=self.LoadUpgrade).pack(side="left", padx=2)
        ttk.Button(BtnFrame, text=self.Lang.Get("Btn_Save"), width=8, command=self.SaveUpgrade).pack(side="left", padx=2)
        
        # 存储升级项数据
        self.UpgradeData = {}
    
    def AddUpgrade(self):
        """添加升级项"""
        Tech = self.UpgradeTechEntry.get().strip()
        Property = self.UpgradePropertyEntry.get().strip()
        Value = self.UpgradeValueEntry.get().strip()
        
        # 验证必填项
        MissingFields = []
        if not Tech:
            MissingFields.append("科技名称")
        if not Property:
            MissingFields.append("升级项")
        if not Value:
            MissingFields.append("数值")
            
        if MissingFields:
            messagebox.showwarning(
                self.Lang.Get("Msg_Warning"),
                f"以下必填项不能为空：\n" + "\n".join([f"• {field}" for field in MissingFields])
            )
            return
        
        SetChecked = "√" if self.UpgradeSetVar.get() else ""
        AddChecked = "√" if self.UpgradeAddVar.get() else ""
        
        # 检查是否已存在
        for Item in self.UpgradeTable.get_children():
            Values = self.UpgradeTable.item(Item, "values")
            if Values and Values[0] == Tech and Values[3] == Property:
                messagebox.showwarning(
                    self.Lang.Get("Msg_Warning"),
                    f"升级项已存在：\n科技：{Tech}\n升级项：{Property}"
                )
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
        ButtonFrame = ttk.Frame(self.ButtonFrame)
        ButtonFrame.pack(side="bottom", anchor="se", padx=5, pady=5)
        
        ttk.Button(ButtonFrame, text="Debug",
                   command=self.DebugPrintWindowSize).pack(side="left", padx=5)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Clear"),
                   command=self.ClearAll).pack(side="left", padx=5)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Default"),
                   command=self.FillDefault).pack(side="left", padx=5)
        ttk.Button(ButtonFrame, text=self.Lang.Get("Btn_Generate"),
                   command=self.GenerateCode).pack(side="left", padx=5)
    
    def DebugPrintWindowSize(self):
        """Debug: 打印当前窗口大小"""
        Width = self.Root.winfo_width()
        Height = self.Root.winfo_height()
        print(f"当前窗口大小: {Width} x {Height}")
    
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
        
        # 基础属性（紧跟单位名称，不加空行）
        BasicLines = self.BuildBasicInfoCode()
        if BasicLines:
            Lines.extend(BasicLines)
        
        # 辅助函数：添加模块代码并插入空行
        def AddModule(ModuleLines):
            if ModuleLines:
                Lines.append("")  # 先加空行
                Lines.extend(ModuleLines)
        
        # 行为控制
        AddModule(self.BuildBehaviorCode())
        
        # 生产单位
        AddModule(self.BuildProducesCode())
        
        # 搭载单位
        AddModule(self.BuildCanCarryCode())
        
        # 航线配置和子单位配置（合并，不在它们之间加空行）
        AirwayLines = self.BuildAirwayCode()
        HostLines = self.BuildCanHostAircraftsCode()
        CombinedLines = []
        if AirwayLines:
            CombinedLines.extend(AirwayLines)
        if HostLines:
            CombinedLines.extend(HostLines)
        AddModule(CombinedLines)
        
        # 武器配置
        AddModule(self.BuildWeaponCode())
        
        # 雷达配置
        AddModule(self.BuildRadarCode())
        
        # 修改器配置
        AddModule(self.BuildModifierCode())
        
        # 状态切换
        AddModule(self.BuildStateCode())
        
        # 升级项
        AddModule(self.BuildUpgradeCode())
        
        # 自定义参数
        CustomLines = []
        for Item in self.CustomParamsTable.get_children():
            Values = self.CustomParamsTable.item(Item, "values")
            if Values and len(Values) >= 2:
                CustomLines.append(f'    {Values[0]} {Values[1]}')
        AddModule(CustomLines)
        
        return "\n".join(Lines)
    
    def BuildBasicInfoCode(self):
        """生成基础信息代码"""
        Lines = []
        
        # 基础数据字段
        BasicFields = [
            ("Tech", "Tech", True),
            ("Movie", "Movie", True),
            ("AbstractMovie", "AbstractMovie", True),
            ("Model", "Model", True),
            ("Icon", "Icon", True),
            ("RoundIcon", "RoundIcon", True),
            ("Type", "Type", False),
            ("Class", "Class", True), # Class 通常需要引号
            ("DrawSize", "DrawSize", False),
            ("AbstractDrawSize", "AbstractDrawSize", False),
            ("LaunchMeSound", "LaunchMeSound", False),
            ("LaunchMePathIcon", "LaunchMePathIcon", True),
            ("DrawOrder", "DrawOrder", False),
            ("Crash", "Crash", True)
        ]
        
        for VarKey, OutputKey, Quoted in BasicFields:
            Value = self.BasicInfoVars.get(VarKey, tk.StringVar()).get()
            if Value:
                if Quoted:
                    Lines.append(f'    {OutputKey} "{Value}"')
                else:
                    Lines.append(f'    {OutputKey} {Value}')
        
        # 特殊处理 Sound 和 Volume (放在基础数据最后)
        Sound = self.BasicInfoVars.get("Sound", tk.StringVar()).get()
        if Sound:
            Volume = self.BasicInfoVars.get("SoundVolume", tk.StringVar()).get()
            if Volume:
                Lines.append(f'    Sound {Sound} Volume {Volume}')
            else:
                Lines.append(f'    Sound {Sound}')
        
        # 属性数据字段
        PropertyFields = [
            ("Power", "Power", False),
            ("Speed", "Speed", False),
            ("TurnSpeed", "TurnSpeed", False),
            ("Size", "Size", False),
            ("Range", "Range", False),
            ("ProductionCost", "ProductionCost", False),
            ("SelfDestruct", "SelfDestructTime", False),
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
        
        PropertyLines = []
        for VarKey, OutputKey, Quoted in PropertyFields:
            Value = self.BasicInfoVars.get(VarKey, tk.StringVar()).get()
            if Value:
                if Quoted:
                    PropertyLines.append(f'    {OutputKey} "{Value}"')
                else:
                    PropertyLines.append(f'    {OutputKey} {Value}')
        
        # 如果有属性数据，先加空行再添加
        if PropertyLines:
            if Lines:
                Lines.append("")
            Lines.extend(PropertyLines)
            
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
            for Item in Items:
                Values = self.ModifierTable.item(Item, "values")
                if Values and Values[0]:
                    Lines.append(f'    Modifier "{Values[0]}"')
        return Lines
    
    def BuildProducesCode(self):
        """生成生产单位代码"""
        Lines = []
        Items = self.ProducesTable.get_children()
        if Items:
            for Item in Items:
                Values = self.ProducesTable.item(Item, "values")
                if Values and Values[0]:
                    Lines.append(f'    Produces "{Values[0]}"')
        return Lines
    
    def BuildCanCarryCode(self):
        """生成搭载单位代码"""
        Lines = []
        Items = self.CanCarryTable.get_children()
        if Items:
            for Item in Items:
                Values = self.CanCarryTable.item(Item, "values")
                if Values and Values[0]:
                    Lines.append(f'    CanCarryUnit "{Values[0]}"')
        return Lines
    
    def BuildAirwayCode(self):
        """生成航线配置代码"""
        Lines = []
        Items = self.AirwayTable.get_children()
        if Items:
            for Item in Items:
                Values = self.AirwayTable.item(Item, "values")
                if Values and len(Values) >= 2:
                    Lines.append(f'    Airway Launch {Values[0]} Time {Values[1]}')
        return Lines
    
    def BuildCanHostAircraftsCode(self):
        """生成子单位配置代码"""
        Lines = []
        Items = self.HostTable.get_children()
        if Items:
            for Item in Items:
                Values = self.HostTable.item(Item, "values")
                if Values and len(Values) >= 2:
                    UnitName = Values[0]
                    Count = Values[1]
                    Airway = Values[2] if len(Values) > 2 and Values[2] else ""
                    Patrol = Values[3] if len(Values) > 3 and Values[3] else ""
                    AutoPatrol = Values[4] if len(Values) > 4 else ""
                    
                    # 格式: CanHostAircrafts [Airway X] "Unit" Count [Patrol Y] [AIAutoPatrol]
                    Parts = ["    CanHostAircrafts"]
                    
                    if Airway:
                        Parts.append(f"Airway {Airway}")
                    
                    Parts.append(f'"{UnitName}"')
                    Parts.append(f"{Count}")
                    
                    if Patrol:
                        Parts.append(f"Patrol {Patrol}")
                    
                    if AutoPatrol == "√":
                        Parts.append("AIAutoPatrol")
                    
                    Lines.append(" ".join(Parts))
        return Lines
    
    def BuildWeaponCode(self):
        """生成武器配置代码"""
        Lines = []
        
        for ConfigName, ConfigInfo in self.ConfigData.items():
            Weapons = ConfigInfo.get("Weapons", [])
            if not Weapons and ConfigName == "Default":
                continue  # Default配置没有武器时不输出
            
            if not Weapons:
                continue
            
            # 构建Config行
            ConfigParts = [f'    Config "{ConfigName}"']
            
            if ConfigInfo.get("Default"):
                ConfigParts.append("Default")
            if ConfigInfo.get("OnlyFull"):
                ConfigParts.append("OnlyFull")
            
            Lines.append(" ".join(ConfigParts))
            
            # 添加武器
            for Weapon in Weapons:
                WeaponParts = [f'        Weapon "{Weapon["Name"]}" {Weapon["Count"]}']
                
                if Weapon.get("Launch"):
                    WeaponParts.append(f'Launch {Weapon["Launch"]}')
                if Weapon.get("Time"):
                    WeaponParts.append(f'Time {Weapon["Time"]}')
                if Weapon.get("AutoEngage"):
                    WeaponParts.append("AutoEngage")
                if Weapon.get("Principal"):
                    WeaponParts.append("Principal")
                if Weapon.get("DefaultOff"):
                    WeaponParts.append("DefaultOff")
                
                Lines.append(" ".join(WeaponParts))
        
        return Lines
    
    def BuildStateCode(self):
        """生成状态切换代码"""
        Lines = []
        
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
            for Item in Items:
                Values = self.UpgradeTable.item(Item, "values")
                if Values and len(Values) >= 5:
                    Tech = Values[0]
                    SetChecked = Values[1] == "√"
                    AddChecked = Values[2] == "√"
                    Property = Values[3]
                    Value = Values[4]
                    
                    # 构建升级项代码
                    UpgradeLine = f'    ImprovedBy "{Tech}"'
                    
                    # 添加Set或Add选项
                    if AddChecked:
                        UpgradeLine += f' Add {Property} {Value}'
                    elif SetChecked:
                        UpgradeLine += f' Set {Property} {Value}'
                    else:
                        # 如果都没有勾选，只输出科技名称
                        pass
                    
                    Lines.append(UpgradeLine)
        
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
