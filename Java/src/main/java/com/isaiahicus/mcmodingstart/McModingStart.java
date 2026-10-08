package com.isaiahicus.mcmodingstart;

import com.isaiahicus.mcmodingstart.item.ModdedItems;
import net.fabricmc.api.ModInitializer;

public final class McModingStart implements ModInitializer {
    public static final String MOD_ID = "mcmodingstart";

    @Override
    public void onInitialize() {
        ModdedItems.registerItems();

        // Common mod initialization goes here.
    }
}
