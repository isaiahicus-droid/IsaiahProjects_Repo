package com.isaiahicus.mcmodingstart.item;

import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.item.Item;
import net.minecraft.item.SwordItem;
import net.minecraft.item.ToolMaterials;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class ModdedItems {
    public static final Item COOL_SWORD = new SwordItem(ToolMaterials.DIAMOND,3, -2.4f, new Item.Settings());

    private static Item registerItem(String name, Item item) {
        return Registry.register(Registries.ITEM, new Identifier.of("mcmodingstart", name), item);
    }

    public static void registerItems() {

    }
}
