package com.isaiahicus.mcmodingstart.item;

import com.isaiahicus.mcmodingstart.McModingStart;
import net.fabricmc.fabric.api.creativetab.v1.CreativeModeTabEvents;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ToolMaterial;

public final class ModdedItems {
    public static final Item COOL_SWORD = registerItem(
            "cool_sword",
            new Item.Properties().sword(ToolMaterial.DIAMOND, 3.0F, -2.4F)
    );

    private ModdedItems() {
    }

    private static Item registerItem(String name, Item.Properties properties) {
        Identifier id = Identifier.fromNamespaceAndPath(McModingStart.MOD_ID, name);
        ResourceKey<Item> itemKey = ResourceKey.create(Registries.ITEM, id);
        return Registry.register(BuiltInRegistries.ITEM, id, new Item(properties.setId(itemKey)));
    }

    public static void registerItems() {
        ResourceKey<CreativeModeTab> combatTab = ResourceKey.create(
                Registries.CREATIVE_MODE_TAB,
                Identifier.withDefaultNamespace("combat")
        );
        CreativeModeTabEvents.modifyOutputEvent(combatTab)
                .register(entries -> entries.accept(COOL_SWORD));
    }
}