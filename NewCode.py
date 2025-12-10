import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

# =============================================================================
# 1. 通用组件类 (Reusable Components)
# =============================================================================

class EditableTable(ttk.Frame):
    """
    通用的可编辑表格组件。
    包含：一个 Treeview，滚动条，以及添加/删除/清空按钮。
    """
    def __init__(self, parent, columns, column_widths=None, height=8):
        super().__init__(parent)
        
        # 1. 创建表格区域
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(side='top', fill='both', expand=True)
        
        # 滚动条
        self.scrollbar = ttk.Scrollbar(self.tree_frame)
        self.scrollbar.pack(side='right', fill='y')
        
        # 表格
        self.tree = ttk.Treeview(
            self.tree_frame, 
            columns=columns, 
            show='headings', 
            height=height,
            yscrollcommand=self.scrollbar.set
        )
        self.scrollbar.config(command=self.tree.yview)
        
        # 设置列头和宽度
        for i, col in enumerate(columns):
            self.tree.heading(col, text=col)
            if column_widths and i < len(column_widths):
                self.tree.column(col, width=column_widths[i])
            else:
                self.tree.column(col, width=100) # 默认宽度
                
        self.tree.pack(side='left', fill='both', expand=True)
        
        # 2. 创建输入区域 (由子类或外部调用者填充)
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(side='top', fill='x', pady=5)
        
        # 3. 创建按钮区域
        self.btn_frame = ttk.Frame(self)
        self.btn_frame.pack(side='bottom', fill='x', pady=5)
        
        # 默认按钮
        ttk.Button(self.btn_frame, text="添加", command=self.add_item).pack(side='left', padx=5)
        ttk.Button(self.btn_frame, text="删除选中", command=self.delete_selected).pack(side='left', padx=5)
        ttk.Button(self.btn_frame, text="清空", command=self.clear_all).pack(side='left', padx=5)

        # 用于存储输入框控件的列表，方便获取数据
        self.input_entries = []

    def add_input_field(self, label_text, width=15, widget_type="entry", values=None):
        """辅助函数：在输入区域添加一个标签和输入框"""
        frame = ttk.Frame(self.input_frame)
        frame.pack(side='left', padx=5)
        ttk.Label(frame, text=label_text).pack(side='left')
        
        if widget_type == "combobox":
            entry = ttk.Combobox(frame, values=values, width=width)
        else:
            entry = ttk.Entry(frame, width=width)
            
        entry.pack(side='left', padx=2)
        self.input_entries.append(entry)
        return entry

    def get_input_values(self):
        """获取所有输入框的当前值"""
        return [entry.get().strip() for entry in self.input_entries]

    def clear_inputs(self):
        """清空所有输入框"""
        for entry in self.input_entries:
            entry.delete(0, tk.END)

    def add_item(self):
        """默认的添加逻辑：读取输入框并添加到表格"""
        values = self.get_input_values()
        if values and values[0]:
            self.tree.insert("", tk.END, values=values)
            self.clear_inputs()
        else:
            messagebox.showwarning("提示", "请至少填写第一项内容")

    def delete_selected(self):
        """删除选中行"""
        selected = self.tree.selection()
        if not selected:
            return
        for item in selected:
            self.tree.delete(item)

    def clear_all(self):
        """清空表格"""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
    def get_all_data(self):
        """获取表格中所有行的数据"""
        data = []
        for item in self.tree.get_children():
            data.append(self.tree.item(item)['values'])
        return data

# =============================================================================
# 2. 标签页模块 (Tab Modules)
# =============================================================================

class BasicInfoTab(ttk.Frame):
    """基础信息标签页 (仅包含常用字段)"""
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        # --- 左侧：基础数据 ---
        self.info_frame = ttk.LabelFrame(self, text="基础数据")
        self.info_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.vars = {}
        
        # 字段定义 (Label, VariableName) - 仅保留 grid.py 原有字段
        fields = [
            ("单位名称 (ID):", "unit_name"),
            ("科技引用 (Tech):", "tech"),
            ("单位类型 (Type):", "type"),
            ("单位类别 (Class):", "class"),
            ("生命值 (Power):", "power"),
            ("移动速度 (Speed):", "speed"),
            ("转向速度 (TurnSpeed):", "turn_speed"),
            ("最大航程 (Range):", "range"),
            ("受击体积 (Size):", "size"),
            ("生产成本 (ProductionCost):", "cost"),
            ("自毁时间 (SelfDestructTime):", "self_destruct"),
            ("自动修复 (AutoRepair):", "auto_repair"),
            ("补给范围 (ResupplyRange):", "resupply_range"),
            ("自动交战范围 (MaxAutoEngageRange):", "auto_engage_range"),
            ("跟随半径 (FollowRadius):", "follow_radius"),
            ("占领半径 (OccupationRadius):", "occupation_radius"),
            ("最小高度 (MinElevation):", "min_elevation"),
            ("最大高度 (MaxElevation):", "max_elevation"),
            ("放置半径 (ProductionPlacementRadius):", "placement_radius"),
            ("绘制顺序 (DrawOrder):", "draw_order"),
            ("最大地图数量 (MaxNumberOnMap):", "max_on_map"),
            ("最大订购数量 (MaxNumberToOrder):", "max_to_order"),
            ("容量需求 (HangarSpaceRequired):", "hangar_required"),
            ("最大载重 (HangarMaxLoad):", "hangar_load"),
            ("爆炸效果 (Crash):", "crash")
        ]
        
        for i, (label, var_name) in enumerate(fields):
            ttk.Label(self.info_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            var = tk.StringVar()
            self.vars[var_name] = var
            
            if var_name == "type":
                ttk.Combobox(self.info_frame, textvariable=var, values=["Ground", "Airborne", "Naval", "Subwater", "Satellite"]).grid(row=i, column=1, sticky="ew", padx=5, pady=2)
            else:
                ttk.Entry(self.info_frame, textvariable=var).grid(row=i, column=1, sticky="ew", padx=5, pady=2)

        # --- 右侧：图形与自定义 ---
        self.right_frame = ttk.Frame(self)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # 图形设置
        self.gfx_frame = ttk.LabelFrame(self.right_frame, text="图形与音效")
        self.gfx_frame.pack(fill="x", pady=5)
        
        gfx_fields = [
            ("俯视图 (Movie):", "movie"),
            ("缩略图 (AbstractMovie):", "abstract_movie"),
            ("3D模型 (Model):", "model"),
            ("图标 (Icon):", "icon"),
            ("圆形图标 (RoundIcon):", "round_icon"),
            ("发射图标路径 (LaunchMePathIcon):", "launch_icon_path"),
            ("图标索引 (IconIDX):", "icon_idx"),
            ("绘制大小 (DrawSize):", "draw_size"),
            ("缩略图大小 (AbstractDrawSize):", "abstract_draw_size"),
            ("模型大小 (ModelDrawSize):", "model_draw_size"),
            ("音效 (Sound):", "sound"),
            ("发射音效 (LaunchMeSound):", "launch_sound")
        ]
        
        for i, (label, var_name) in enumerate(gfx_fields):
            ttk.Label(self.gfx_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            var = tk.StringVar()
            self.vars[var_name] = var
            ttk.Entry(self.gfx_frame, textvariable=var).grid(row=i, column=1, sticky="ew", padx=5, pady=2)

        # 自定义参数表格
        self.custom_frame = ttk.LabelFrame(self.right_frame, text="自定义参数")
        self.custom_frame.pack(fill="both", expand=True, pady=5)
        
        self.custom_table = EditableTable(self.custom_frame, columns=["参数名", "参数值"], column_widths=[150, 150])
        self.custom_table.pack(fill="both", expand=True, padx=5, pady=5)
        self.custom_table.add_input_field("参数名:")
        self.custom_table.add_input_field("参数值:")

    def get_data(self):
        data = {k: v.get() for k, v in self.vars.items()}
        data['custom_params'] = self.custom_table.get_all_data()
        return data


class AdvancedInfoTab(ttk.Frame):
    """高级信息标签页 (Escalation 新增或不常用字段)"""
    def __init__(self, parent):
        super().__init__(parent)
        
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.vars = {}
        
        fields = [
            ("继承自 (COPY):", "copy_from"),
            ("禁用科技 (DisablingTech):", "disabling_tech"),
            ("虚拟速度 (VirtualSpeed):", "virtual_speed"),
            ("传感器激活延迟 (SensorsActivationDelay):", "sensor_delay"),
            ("武器激活延迟 (WeaponsActivationDelay):", "weapon_delay"),
            ("部署延迟 (OnDeployLaunchHostedDelay):", "deploy_delay"),
            ("攻击延迟 (AttackDelay):", "attack_delay"),
            ("衰减计时器 (DecayTimer):", "decay_timer"),
            ("销毁消息 (DestructionMessage):", "destruction_msg")
        ]
        
        for i, (label, var_name) in enumerate(fields):
            ttk.Label(self.main_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            var = tk.StringVar()
            self.vars[var_name] = var
            ttk.Entry(self.main_frame, textvariable=var, width=40).grid(row=i, column=1, sticky="w", padx=5, pady=5)

    def get_data(self):
        return {k: v.get() for k, v in self.vars.items()}


class BehaviorTab(ttk.Frame):
    """行为控制标签页"""
    def __init__(self, parent):
        super().__init__(parent)
        
        self.behavior_frame = ttk.LabelFrame(self, text="行为标记 (Boolean Flags)")
        self.behavior_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # 定义复选框配置 (显示文本, 内部键名)
        self.checkbox_configs = [
            ("在敌方领土可见 (AlwaysVisibleOnEnemyTerritory)", "AlwaysVisibleOnEnemyTerritory"),
            ("受击不触发战争 (DoesNotTriggerWarWhenAttacked)", "DoesNotTriggerWarWhenAttacked"),
            ("攻击不触发战争 (DoesNotTriggerWarOnAttack)", "DoesNotTriggerWarOnAttack"),
            ("和平时期可跨越边界 (CanCrossBorderDuringPeaceTime)", "CanCrossBorderDuringPeaceTime"),
            ("可跨越边界 (CanCrossBorder)", "CanCrossBorder"),
            ("显示被装载于母单位 (ReportAsHosted)", "ReportAsHosted"),
            ("在被攻击名单中 (TargetInPlanner)", "TargetInPlanner"),
            ("在攻击者名单中 (AttackerInPlanner)", "AttackerInPlanner"),
            ("可访问全局武库 (CanAccessGlobalStorage)", "CanAccessGlobalStorage"),
            ("可访问本地武库 (CanAccessWeaponStockpile)", "CanAccessWeaponStockpile"),
            ("可访问单位武库 (CanAccessUnitStockpile)", "CanAccessUnitStockpile"),
            ("可悬停 (CanHangInTheAir)", "CanHangInTheAir"),
            ("隐藏所有者阵营 (HideOwnership)", "HideOwnership"),
            ("可设置巡逻点 (CanPatrolPoint)", "CanPatrolPoint"),
            ("自动返回母单位 (AutoReturn)", "AutoReturn"),
            ("由其他单位生产 (ProducedByAnotherUnit)", "ProducedByAnotherUnit"),
            ("固定朝向 (FixedRotationAngle)", "FixedRotationAngle"),
            ("移动时可攻击 (AttackOnMove)", "AttackOnMove"),
            ("部署时显示禁用 (ShowDisabledOnDeploymentMarker)", "ShowDisabledOnDeploymentMarker"),
            ("投降后自动摧毁 (DestroyOnFactionSurrender)", "DestroyOnFactionSurrender"),
            ("对盟友隐藏 (HiddenFromAllies)", "HiddenFromAllies"),
            ("被摧毁时反击 (AttackIfDestroyed)", "AttackIfDestroyed"),
            ("不自动攻击 (NoAutoAttack)", "NoAutoAttack"),
            ("不自动攻击潜艇 (NoAutoAttackSub)", "NoAutoAttackSub"),
            ("附属于母单位 (Slave)", "Slave"),
            ("不自动部署 (NoAutoDeploy)", "NoAutoDeploy"),
            ("特殊状态 (SpecialState)", "SpecialState"),
            ("被围困时执行命令 (ExecuteOrdersWhenBesieged)", "ExecuteOrdersWhenBesieged"),
            ("战争计划中移动到目标 (MoveToTargetInWarPlan)", "MoveToTargetInWarPlan"),
            ("强制 MipMap (ForceMipMap)", "ForceMipMap"),
            ("隐藏缩略图 (HideAbstract)", "HideAbstract")
        ]
        
        self.vars = {}
        
        # 自动生成复选框，分3列显示
        for i, (text, key) in enumerate(self.checkbox_configs):
            var = tk.BooleanVar()
            self.vars[key] = var
            col = i % 3
            row = i // 3
            ttk.Checkbutton(self.behavior_frame, text=text, variable=var).grid(row=row, column=col, sticky="w", padx=10, pady=5)

    def get_data(self):
        return {k: v.get() for k, v in self.vars.items()}


class StateTab(ttk.Frame):
    """状态切换标签页 (HighState/LowState)"""
    def __init__(self, parent):
        super().__init__(parent)
        
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.vars = {}
        
        # 状态定义
        fields = [
            ("高状态单位 (HighState):", "HighState"),
            ("低状态单位 (LowState):", "LowState"),
            ("切换到高状态时间 (TimeToHighState):", "TimeToHighState"),
            ("切换到低状态时间 (TimeToLowState):", "TimeToLowState"),
            ("高状态文本索引 (HighStateStringIDX):", "HighStateStringIDX"),
            ("低状态文本索引 (LowStateStringIDX):", "LowStateStringIDX"),
            ("状态文本索引 (StateStringIDX):", "StateStringIDX"),
            ("状态图标 (StateIcon):", "StateIcon"),
            ("切换高状态图标 (ToHighStateIcon):", "ToHighStateIcon"),
            ("切换低状态图标 (ToLowStateIcon):", "ToLowStateIcon"),
            ("切换高状态过程文本 (ToHighStateProcessStringIDX):", "ToHighStateProcessStringIDX"),
            ("切换低状态过程文本 (ToLowStateProcessStringIDX):", "ToLowStateProcessStringIDX"),
            ("自动休息延迟 (AutoOnRestDelay):", "AutoOnRestDelay")
        ]
        
        for i, (label, key) in enumerate(fields):
            ttk.Label(self.main_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            var = tk.StringVar()
            self.vars[key] = var
            ttk.Entry(self.main_frame, textvariable=var, width=40).grid(row=i, column=1, sticky="w", padx=5, pady=2)
            
        # 自动切换规则 (Combobox)
        shift_rules = [
            ("撤退切换 (RetreatShift):", "RetreatShift"),
            ("攻击切换 (AttackShift):", "AttackShift"),
            ("防御切换 (DefenceShift):", "DefenceShift"),
            ("快速移动切换 (FastMoveShift):", "FastMoveShift"),
            ("冰下切换 (UnderIceShift):", "UnderIceShift"),
            ("移动切换 (AutoOnMoveShift):", "AutoOnMoveShift"),
            ("休息切换 (AutoOnRest):", "AutoOnRest")
        ]
        
        shift_options = ["", "High", "Low", "None"]
        
        for i, (label, key) in enumerate(shift_rules):
            row = i + len(fields)
            ttk.Label(self.main_frame, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)
            var = tk.StringVar()
            self.vars[key] = var
            ttk.Combobox(self.main_frame, textvariable=var, values=shift_options, width=37).grid(row=row, column=1, sticky="w", padx=5, pady=2)

    def get_data(self):
        return {k: v.get() for k, v in self.vars.items()}


class SubUnitTab(ttk.Frame):
    """子单位与生产标签页"""
    def __init__(self, parent):
        super().__init__(parent)
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # 1. 生产单位 (Produces)
        self.produces_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.produces_frame, text="生产单位 (Produces)")
        self.produces_table = EditableTable(self.produces_frame, columns=["单位名称"])
        self.produces_table.pack(fill='both', expand=True)
        self.produces_table.add_input_field("单位名称:")
        
        # 2. 搭载单位 (CanCarryUnit)
        self.carry_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.carry_frame, text="搭载单位 (CanCarryUnit)")
        self.carry_table = EditableTable(self.carry_frame, columns=["单位名称", "构建(Build)"])
        self.carry_table.pack(fill='both', expand=True)
        self.carry_table.add_input_field("单位名称:")
        self.carry_table.add_input_field("Build (可选):")
        
        # 3. 托管飞机 (CanHostAircrafts)
        self.host_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.host_frame, text="托管飞机 (CanHostAircrafts)")
        self.host_table = EditableTable(self.host_frame, columns=["航线ID", "单位名称", "数量", "巡逻数", "自动巡逻"], column_widths=[50, 150, 50, 50, 80])
        self.host_table.pack(fill='both', expand=True)
        self.host_table.add_input_field("航线ID (可选):", width=5)
        self.host_table.add_input_field("单位名称:")
        self.host_table.add_input_field("数量:", width=5)
        self.host_table.add_input_field("巡逻数:", width=5)
        self.host_table.add_input_field("自动巡逻 (AIAutoPatrol):", width=10, widget_type="combobox", values=["", "AIAutoPatrol"])
        
        # 4. 航线配置 (Airway)
        self.airway_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.airway_frame, text="航线配置 (Airway)")
        self.airway_table = EditableTable(self.airway_frame, columns=["发射数 (Launch)", "间隔时间 (Time)"])
        self.airway_table.pack(fill='both', expand=True)
        self.airway_table.add_input_field("发射数:")
        self.airway_table.add_input_field("间隔时间:")

    def get_data(self):
        return {
            "produces": self.produces_table.get_all_data(),
            "can_carry": self.carry_table.get_all_data(),
            "can_host": self.host_table.get_all_data(),
            "airway": self.airway_table.get_all_data()
        }


class WeaponTab(ttk.Frame):
    """
    武器配置标签页 (复杂逻辑)
    结构：左侧 Config 树，右侧 Weapon 列表
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        self.paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned.pack(fill='both', expand=True, padx=5, pady=5)
        
        # --- 左侧：配置树 (Config / ImprovedBy) ---
        self.left_frame = ttk.LabelFrame(self.paned, text="配置结构 (Config Tree)")
        self.paned.add(self.left_frame, weight=1)
        
        self.tree = ttk.Treeview(self.left_frame, show="tree")
        self.tree.pack(side='left', fill='both', expand=True)
        self.tree_scroll = ttk.Scrollbar(self.left_frame, orient="vertical", command=self.tree.yview)
        self.tree_scroll.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        
        # 树操作按钮
        self.tree_btn_frame = ttk.Frame(self.left_frame)
        self.tree_btn_frame.pack(side='bottom', fill='x')
        ttk.Button(self.tree_btn_frame, text="添加 Config", command=self.add_config).pack(side='left', padx=2)
        ttk.Button(self.tree_btn_frame, text="添加 ImprovedBy", command=self.add_improved_by).pack(side='left', padx=2)
        ttk.Button(self.tree_btn_frame, text="删除节点", command=self.delete_node).pack(side='left', padx=2)
        
        # --- 右侧：武器列表 ---
        self.right_frame = ttk.LabelFrame(self.paned, text="武器列表 (Weapons)")
        self.paned.add(self.right_frame, weight=2)
        
        self.weapon_table = EditableTable(
            self.right_frame, 
            columns=["武器类型", "备弹", "发射数", "时间", "自动接敌", "主武器", "默认关闭"],
            column_widths=[120, 50, 50, 50, 60, 50, 60]
        )
        self.weapon_table.pack(fill='both', expand=True)
        
        # 武器输入
        self.weapon_table.add_input_field("类型:")
        self.weapon_table.add_input_field("备弹:", width=5)
        self.weapon_table.add_input_field("发射数:", width=5)
        self.weapon_table.add_input_field("时间:", width=5)
        self.weapon_table.add_input_field("自动:", width=5, widget_type="combobox", values=["", "AutoEngage"])
        self.weapon_table.add_input_field("主武器:", width=5, widget_type="combobox", values=["", "Principal"])
        self.weapon_table.add_input_field("默认关:", width=5, widget_type="combobox", values=["", "DefaultOff"])
        
        # 绑定事件：点击树节点加载对应的武器数据
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        
        # 数据存储：NodeID -> WeaponList
        self.node_weapons = {}
        
        # 覆盖 add_item 以保存到字典
        self.original_add_item = self.weapon_table.add_item
        self.weapon_table.add_item = self.add_weapon_wrapper
        
        # 覆盖 delete_selected 以更新字典
        self.original_delete_selected = self.weapon_table.delete_selected
        self.weapon_table.delete_selected = self.delete_weapon_wrapper

    def add_config(self):
        name = tk.simpledialog.askstring("输入", "Config 名称:")
        if name:
            # 询问额外属性
            attrs = []
            if messagebox.askyesno("选项", "是否为默认配置 (Default)?"): attrs.append("Default")
            if messagebox.askyesno("选项", "是否仅满载 (OnlyFull)?"): attrs.append("OnlyFull")
            
            text = f"Config \"{name}\" {' '.join(attrs)}"
            node_id = self.tree.insert("", "end", text=text, values=("Config", name, attrs))
            self.node_weapons[node_id] = []

    def add_improved_by(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("提示", "请先选择一个父节点 (Config 或 ImprovedBy)")
            return
        
        parent_id = selected[0]
        name = tk.simpledialog.askstring("输入", "ImprovedBy 科技名称:")
        if name:
            text = f"ImprovedBy \"{name}\""
            node_id = self.tree.insert(parent_id, "end", text=text, values=("ImprovedBy", name))
            self.node_weapons[node_id] = []
            self.tree.item(parent_id, open=True)

    def delete_node(self):
        selected = self.tree.selection()
        if selected:
            node_id = selected[0]
            self.tree.delete(node_id)
            if node_id in self.node_weapons:
                del self.node_weapons[node_id]

    def on_tree_select(self, event):
        # 保存当前表格数据到上一个选中的节点 (如果需要实时保存，这里简化为切换时刷新)
        # 实际上，因为我们直接操作了 self.node_weapons，所以只需要刷新显示
        selected = self.tree.selection()
        if not selected:
            return
        
        node_id = selected[0]
        self.refresh_weapon_table(node_id)

    def refresh_weapon_table(self, node_id):
        self.weapon_table.clear_all()
        weapons = self.node_weapons.get(node_id, [])
        for w in weapons:
            self.weapon_table.tree.insert("", "end", values=w)

    def add_weapon_wrapper(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("提示", "请先在左侧选择一个配置节点")
            return
        
        node_id = selected[0]
        values = self.weapon_table.get_input_values()
        if values and values[0]:
            self.node_weapons[node_id].append(values)
            self.refresh_weapon_table(node_id)
            self.weapon_table.clear_inputs()

    def delete_weapon_wrapper(self):
        selected_node = self.tree.selection()
        if not selected_node: return
        
        node_id = selected_node[0]
        selected_items = self.weapon_table.tree.selection()
        
        # 从后往前删，防止索引偏移
        for item in reversed(selected_items):
            idx = self.weapon_table.tree.index(item)
            if idx < len(self.node_weapons[node_id]):
                self.node_weapons[node_id].pop(idx)
        
        self.refresh_weapon_table(node_id)

    def get_data(self):
        # 递归构建数据结构
        def get_node_data(item_id):
            item = self.tree.item(item_id)
            data = {
                "text": item['text'],
                "type": item['values'][0] if item['values'] else "",
                "weapons": self.node_weapons.get(item_id, []),
                "children": []
            }
            for child_id in self.tree.get_children(item_id):
                data["children"].append(get_node_data(child_id))
            return data

        roots = []
        for child_id in self.tree.get_children(""):
            roots.append(get_node_data(child_id))
        return roots


class RadarModifierTab(ttk.Frame):
    """雷达与修改器标签页"""
    def __init__(self, parent):
        super().__init__(parent)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        # 雷达
        self.radar_frame = ttk.LabelFrame(self, text="雷达配置 (Radar)")
        self.radar_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.radar_table = EditableTable(self.radar_frame, columns=["雷达类型", "默认关闭"])
        self.radar_table.pack(fill='both', expand=True)
        self.radar_table.add_input_field("雷达类型:")
        self.radar_table.add_input_field("默认关闭:", widget_type="combobox", values=["", "DefaultOff"])
        
        # 修改器
        self.mod_frame = ttk.LabelFrame(self, text="修改器 (Modifier)")
        self.mod_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.mod_table = EditableTable(self.mod_frame, columns=["修改器名称", "数值 (可选)"])
        self.mod_table.pack(fill='both', expand=True)
        self.mod_table.add_input_field("修改器名称:")
        self.mod_table.add_input_field("数值:")

    def get_data(self):
        return {
            "radars": self.radar_table.get_all_data(),
            "modifiers": self.mod_table.get_all_data()
        }


class UpgradeTab(ttk.Frame):
    """升级项标签页 (ImprovedBy)"""
    def __init__(self, parent):
        super().__init__(parent)
        
        self.upgrade_table = EditableTable(self, columns=["科技名称", "属性", "值/操作"], column_widths=[150, 150, 150])
        self.upgrade_table.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.upgrade_table.add_input_field("科技名称:")
        self.upgrade_table.add_input_field("属性 (如 Speed):")
        self.upgrade_table.add_input_field("值 (如 1.1 或 Set Speed 50):", width=30)

    def get_data(self):
        return self.upgrade_table.get_all_data()


# =============================================================================
# 3. 代码生成器 (Code Generator)
# =============================================================================

class CodeGenerator:
    @staticmethod
    def generate(app):
        lines = []
        
        # 1. 基础信息
        basic = app.tab_basic.get_data()
        advanced = app.tab_advanced.get_data()
        
        unit_name = basic.get('unit_name', 'NewUnit')
        copy_from = advanced.get('copy_from', '')
        
        if copy_from:
            lines.append(f'[UNIT] "{unit_name}" COPY "{copy_from}"')
        else:
            lines.append(f'[UNIT] "{unit_name}"')
            
        # 基础字段映射
        simple_fields = {
            'tech': 'Tech', 'type': 'Type', 'class': 'Class',
            'power': 'Power', 'speed': 'Speed', 
            'turn_speed': 'TurnSpeed', 'range': 'Range', 'size': 'Size',
            'cost': 'ProductionCost', 'self_destruct': 'SelfDestructTime',
            'auto_repair': 'AutoRepair', 'resupply_range': 'ResupplyRange',
            'auto_engage_range': 'MaxAutoEngageRange', 'follow_radius': 'FollowRadius',
            'occupation_radius': 'OccupationRadius', 'min_elevation': 'MinElevation',
            'max_elevation': 'MaxElevation', 'placement_radius': 'ProductionPlacementRadius',
            'draw_order': 'DrawOrder', 'max_on_map': 'MaxNumberOnMap',
            'max_to_order': 'MaxNumberToOrder', 'hangar_required': 'HangarSpaceRequired',
            'hangar_load': 'HangarMaxLoad', 'crash': 'Crash',
            'movie': 'Movie', 'abstract_movie': 'AbstractMovie', 'model': 'Model',
            'icon': 'Icon', 'round_icon': 'RoundIcon', 'launch_icon_path': 'LaunchMePathIcon',
            'icon_idx': 'IconIDX', 'draw_size': 'DrawSize', 'abstract_draw_size': 'AbstractDrawSize',
            'model_draw_size': 'ModelDrawSize', 'sound': 'Sound', 'launch_sound': 'LaunchMeSound'
        }
        
        # 高级字段映射
        advanced_fields = {
            'disabling_tech': 'DisablingTech', 'virtual_speed': 'VirtualSpeed',
            'sensor_delay': 'SensorsActivationDelay', 'weapon_delay': 'WeaponsActivationDelay',
            'deploy_delay': 'OnDeployLaunchHostedDelay', 'attack_delay': 'AttackDelay',
            'decay_timer': 'DecayTimer', 'destruction_msg': 'DestructionMessage'
        }
        
        # 处理基础字段
        for key, label in simple_fields.items():
            val = basic.get(key)
            if val:
                if key == 'sound' and ',' in val:
                    parts = val.split(',')
                    lines.append(f"  {label} {parts[0].strip()} Volume {parts[1].strip()}")
                elif key == 'launch_icon_path':
                     lines.append(f"  {label} element \"{val}\"")
                elif key in ['movie', 'abstract_movie', 'model', 'icon', 'round_icon', 'tech', 'class', 'crash']:
                    lines.append(f"  {label} \"{val}\"")
                else:
                    lines.append(f"  {label} {val}")

        # 处理高级字段
        for key, label in advanced_fields.items():
            val = advanced.get(key)
            if val:
                if key in ['disabling_tech', 'destruction_msg']:
                    lines.append(f"  {label} \"{val}\"")
                else:
                    lines.append(f"  {label} {val}")

        # 自定义参数
        for row in basic['custom_params']:
            lines.append(f"  {row[0]} {row[1]}")

        # 2. 行为标记
        behavior = app.tab_behavior.get_data()
        for key, val in behavior.items():
            if val:
                lines.append(f"  {key} Yes")

        # 3. 状态切换
        state = app.tab_state.get_data()
        for key, val in state.items():
            if val:
                if "Icon" in key:
                    lines.append(f"  {key} \"{val}\"")
                else:
                    lines.append(f"  {key} {val}")

        # 4. 子单位
        sub = app.tab_sub.get_data()
        for row in sub['produces']:
            lines.append(f"  Produces \"{row[0]}\"")
        for row in sub['can_carry']:
            val = f"  CanCarryUnit \"{row[0]}\""
            if len(row) > 1 and row[1]: val += f" {row[1]}"
            lines.append(val)
        for row in sub['airway']:
            lines.append(f"  Airway Launch {row[0]} Time {row[1]}")
        for row in sub['can_host']:
            line = "  CanHostAircrafts"
            if row[0]: line += f" airway {row[0]}"
            line += f" \"{row[1]}\" {row[2]}"
            if row[3]: line += f" Patrol {row[3]}"
            if row[4]: line += f" {row[4]}"
            lines.append(line)

        # 5. 雷达与修改器
        rm = app.tab_radar.get_data()
        for row in rm['radars']:
            line = f"  Radar \"{row[0]}\""
            if len(row) > 1 and row[1]: line += f" {row[1]}"
            lines.append(line)
        for row in rm['modifiers']:
            line = f"  Modifier \"{row[0]}\""
            if len(row) > 1 and row[1]: line += f" {row[1]}"
            lines.append(line)

        # 6. 升级项
        upgrades = app.tab_upgrade.get_data()
        for row in upgrades:
            lines.append(f"  ImprovedBy \"{row[0]}\" {row[1]} {row[2]}")

        # 7. 武器配置
        weapon_roots = app.tab_weapon.get_data()
        
        def write_node(node, indent_level=1):
            indent = "  " * indent_level
            lines.append(f"{indent}{node['text']}")
            
            for w in node['weapons']:
                w_line = f"{indent}  Weapon \"{w[0]}\""
                if w[1]: w_line += f" {w[1]}"
                if w[2]: w_line += f" Launch {w[2]}"
                if w[3]: w_line += f" Time {w[3]}"
                if w[4]: w_line += f" {w[4]}"
                if w[5]: w_line += f" {w[5]}"
                if w[6]: w_line += f" {w[6]}"
                lines.append(w_line)
            
            if node['children']:
                lines.append(f"{indent}{{")
                for child in node['children']:
                    write_node(child, indent_level + 1)
                lines.append(f"{indent}}}")

        for root in weapon_roots:
            write_node(root)

        return "\n".join(lines)


# =============================================================================
# 4. 主程序类 (Main Application)
# =============================================================================

class UnitGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ICBM Escalation Unit Generator (NewCode)")
        self.root.geometry("1200x800")
        
        # 菜单栏
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="生成代码", command=self.generate_code)
        file_menu.add_command(label="退出", command=root.quit)
        menubar.add_cascade(label="文件", menu=file_menu)
        root.config(menu=menubar)
        
        # 主容器
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # 初始化标签页
        self.tab_basic = BasicInfoTab(self.notebook)
        self.tab_advanced = AdvancedInfoTab(self.notebook)
        self.tab_behavior = BehaviorTab(self.notebook)
        self.tab_state = StateTab(self.notebook)
        self.tab_sub = SubUnitTab(self.notebook)
        self.tab_weapon = WeaponTab(self.notebook)
        self.tab_radar = RadarModifierTab(self.notebook)
        self.tab_upgrade = UpgradeTab(self.notebook)
        
        # 添加到 Notebook
        self.notebook.add(self.tab_basic, text="基础信息")
        self.notebook.add(self.tab_advanced, text="高级信息")
        self.notebook.add(self.tab_behavior, text="行为控制")
        self.notebook.add(self.tab_state, text="状态切换")
        self.notebook.add(self.tab_sub, text="子单位/生产")
        self.notebook.add(self.tab_weapon, text="武器配置")
        self.notebook.add(self.tab_radar, text="雷达/修改器")
        self.notebook.add(self.tab_upgrade, text="升级项")
        
        # 底部按钮
        btn_frame = ttk.Frame(root)
        btn_frame.pack(side='bottom', fill='x', padx=10, pady=10)
        ttk.Button(btn_frame, text="生成代码", command=self.generate_code).pack(side='right')

    def generate_code(self):
        code = CodeGenerator.generate(self)
        
        # 显示结果窗口
        top = tk.Toplevel(self.root)
        top.title("生成的代码")
        top.geometry("800x600")
        
        text = tk.Text(top, font=("Consolas", 10))
        text.pack(fill='both', expand=True)
        text.insert(tk.END, code)

if __name__ == "__main__":
    root = tk.Tk()
    
    # 设置主题
    style = ttk.Style()
    try:
        style.theme_use('vista')
    except:
        style.theme_use('clam')
        
    # 全局样式调整
    style.configure('.', font=('Microsoft YaHei UI', 9))
    style.configure('Treeview', rowheight=25)
    
    # 简单的 simpledialog 实现，避免引入额外依赖
    import tkinter.simpledialog
    
    app = UnitGeneratorApp(root)
    root.mainloop()
