package com.isaiahicus.mcmodingstart;

import net.fabricmc.api.ModInitializer;

public final class McModingStart implements ModInitializer {
    public static final String MOD_ID = "mcmodingstart";
    public static final Item EXAMPLE_ITEM = new Item(new Item.Settings());
    @Override
    public void onInitialize() {
     ModdedItems.registerItems();
     
        // Common mod initialization goes here.
    }
}
